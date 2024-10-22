# SCA.py
# Authors:
# Lars Vermeulen <lars.larsvermeulen@gmail.com>
# Simon Vandevelde <s.vandevelde@kuleuven.be>
import re
import argparse
import time
from fileinput import filename
from textx import get_location

try:
    from ast_engine.Parse import IDP
    from ast_engine.utils import IDPZ3Error
except ModuleNotFoundError:
    from .ast_engine.Parse import IDP
    from .ast_engine.utils import IDPZ3Error


def output(err, err_type):
    """ Format the output as
    'warning/error: line .. - colStart .. - colEnd => message'
    """
    format_str = ''
    format_str += f"-- {err_type} : number = {len(err)}\n"
    for i in err:
        location = get_location(i[0])
        if hasattr(i[0], 'name'):
            colEnd = location['col'] + len(i[0].name)
        elif hasattr(i[0], 'annotations') and i[0].annotations is not None:
            colEnd = location['col'] + len(i[0].annotations['reading'])
        else:
            colEnd = location['col']
        format_str += (f"{i[2]}: line {location['line']} -"
                       f" colStart {location['col']} -"
                       f" colEnd {colEnd} => {i[1]}\n")
    return format_str


def perform_check(A):
    """ Lint a node and its children recursively. """
    detections = []
    A.SCA_Check(detections)
    warnings = []
    errors = []
    for i in detections:
        # Split in warnings and errors.
        if i[2] == "Warning":
            warnings.append(i)
        else:
            errors.append(i)
    output_str = output(errors, "Error")
    output_str += output(warnings, "Warning")
    return (len(detections), output_str)


def sca(idp):
    """ Lint each voc, struc, theory and procedure block. """
    number = 0
    output_str = "\n---------- Vocabulary Check ----------\n"
    for v in idp.vocabularies:
        output_str += f"----- {v}\n"
        V = idp.get_blocks(v)
        new_number, new_output = perform_check(V[0])
        output_str += new_output
        number += new_number
    output_str += "\n---------- Structure Check ----------\n"
    for s in idp.structures:
        output_str += f"----- {s}\n"
        S = idp.get_blocks(s)
        new_number, new_output = perform_check(S[0])
        output_str += new_output
        number += new_number
    output_str += "\n---------- Theory Check ----------\n"
    for t in idp.theories:
        output_str += f"----- {t}\n"
        T = idp.get_blocks(t)
        new_number, new_output = perform_check(T[0])
        output_str += new_output
        number += new_number
    output_str += "\n---------- Procedure Check ----------\n"
    for p in idp.procedures:
        output_str += f"----- {p}\n"
        P = idp.get_blocks(p)
        new_number, new_output = perform_check(P[0])
        output_str += new_output
        number += new_number
    return (number, output_str)


def extra(file):
    """ Detect some additional style guide errors, which are not done via the
    AST but instead using the source file directly.

    This is done because the AST e.g. abstracts away all spaces.
    """
    detections = []
    # Check for errors, and format them.
    extra_check(file, detections)
    output_str = extra_output(detections)
    return len(detections), output_str


def extra_check(file, detections):
    pattern2 = re.compile(r"\/\/")  # Comments
    consistence = ''
    consistence_help = False
    unicode_symbols = ['⨯', '→', '𝔹', 'ℤ', 'ℝ', '∀', '∃', '∈', '∉', '←', '∧',
                       '∨', '¬', '⇒', '⇔', '⇐', '≤', '≠', '≥']
    ascii_symbols = ['*', '->', ' Bool ', ' Int ', ' Real ', '!', '?', ' in ',
                     '<-', '&', '~', '=>', '<=>', '<=', '=<',
                     '~=', '>=']
    cur_block = None
    for line_number, line in enumerate(file.split('\n'), start=1):
        # Set the current block.
        if 'ocabulary' in line:
            cur_block = 'voc'
        elif 'tructure' in line:
            cur_block = 'struct'
        elif 'heory' in line:
            cur_block = 'theory'
        elif 'rocedure' in line:
            cur_block = 'main'

        if cur_block == 'main':
            # Don't perform style checks on the main.
            continue

        # Ignore annotations.
        if line.strip().startswith('['):
            continue

        # Some symbols should have a space in front.
        for match in re.finditer(r'[\w\)\d][*⨯><→⇒⇔≤≠≥=∉∈∧∨&|]', line):
            str_match = match.string[match.start():match.end()]
            # If a > is found in a URI, ignore it.
            if (str_match.endswith('>') and
                re.findall((r'<https?:\/\/((\w*\.)?)*(\w+\/)*\w+#(\w+)?' +
                            str_match),
                           line)):
                continue

            symbol = match.group()[1]
            detections.append((line_number, match.span()[0], match.span()[1],
                               f"Style: space in front of '{symbol}'",
                               "Warning"))

        # Some symbols should be followed by a space.
        for match in re.finditer(r'[,*⨯><→⇒⇔≤≠≥=∉∈][\w\d]', line):
            symbol = match.group()[0]
            str_match = match.string[match.start():match.end()]
            # If a < is found in a URI, ignore it.
            if (str_match.startswith('<') and
                re.findall((str_match +
                            r'h?t?tps?:\/\/((\w*\.)?)*(\w+\/)*\w+#(\w+)?>'),
                           line)):
                continue
            # Also ignore generalised existential quantifiers
            if line[match.start()-1] in '?=':
                continue

            detections.append((line_number, match.span()[0], match.span()[1],
                               f"Style: space after '{symbol}'",
                               "Warning"))

        # Some symbols should not be followed by a space.
        for match in re.finditer(r'[~¬]\s', line):
            symbol = match.group()[0]
            detections.append((line_number, match.span()[0], match.span()[1],
                               f"Style: no space allowed after '{symbol}'",
                               "Warning"))

        # Don't allow multiple rules on the same line.
        if line.count('. ') > 1:
            detections.append((line_number, 0, len(line),
                               "Style: use new line for new rule",
                               "Warning"))

        # Correct use of indentation
        if not(line.startswith('\t') or line.startswith('    ') or line.startswith('//')):
            keywords = ["vocabulary", "structure", "theory", "procedure", "}",
                        "display", "prefix"]
            if not(len(line.strip()) == 0
                   or any(word in line for word in keywords)):
                detections.append((line_number, 0, 4,
                                   "Style: incorrect indentation", "Warning"))

        # Consistent use of unicode or ASCII (if not a comment)
        if re.match(pattern2, line.strip()):
            continue
        if not(consistence_help):
            if any(symbol in line for symbol in unicode_symbols):
                consistence = "unicode"
                consistence_help = True
            elif any(symbol in line for symbol in ascii_symbols):
                consistence = "ASCII"
                consistence_help = True
        else:
            if (any(symbol in line for symbol in unicode_symbols) and
                    any(symbol in line for symbol in ascii_symbols)):
                detections.append((line_number, 0, 4,
                                   "Style: don't mix unicode and ASCII",
                                   "Warning"))
            elif (any(symbol in line for symbol in unicode_symbols) and
                    consistence == "ASCII"):
                detections.append((line_number, 0, 4,
                                   "Style: don't mix unicode and ASCII",
                                   "Warning"))
            elif (any(symbol in line for symbol in ascii_symbols) and
                    consistence == "unicode"):
                detections.append((line_number, 0, 4,
                                   "Style: don't mix unicode and ASCII",
                                   "Warning"))

    return detections


def extra_output(err):
    """ Output of extra style guide warning in format
        'warning: line .. - colStart .. - colEnd=> message' """
    output_str = f"\n---------- Number extra style check: {len(err)} ----------\n"
    for i in err:
        output_str += f"{i[4]}: line {i[0]} - colStart {i[1]} - colEnd {i[2]} => {i[3]}\n"
    return output_str


def lint_fo(idp_file, timing=True, print_ast=False):
    """ Lint FO(.) """
    start_time = time.time()
    output_str = ''
    try:
        total = 0
        idp = IDP.from_str(idp_file)  # Parse IDP file to AST.

        # Execute the SCA!
        total, output_str = sca(idp)

        # Apply non-AST checks.
        number, extra_str = extra(idp_file)
        total += number
        output_str += extra_str

        output_str += "\n".join(str(msg) for msg in idp.warnings)

        output_str += f"\n---------- Total number detections: {total} ----------\n"

    except IDPZ3Error as e1:
        output_str += "\n---------- Syntax Error ----------\n" + str(e1) + "\n"

    except KeyError as e2:  # In case of KeyError
        output_str += f"Error: line {0} - colStart {0} - colEnd {0} => Key Error {e2}\n"

    except Exception as e:
        output_str += str(e) + '\n'
        output_str += "\n---------- Syntax Error ----------\n"
        try:
            output_str += f"{filename}: Error: line {e.line} - colStart {e.col} - colEnd {e.col} => {e.args}\n"
        except:  # In case of an error without line number.
            output_str += f"{filename}: Error: line {0} - colStart {0} - colEnd {10} => {e}\n"

    if timing:
        output_str += f"\nElapsed time: {format(time.time() - start_time)} seconds\n"
    return output_str


def main():
    parser = argparse.ArgumentParser(description='SCA')
    parser.add_argument('FILE', help='path to the .idp file')
    parser.add_argument('--no-timing', help='don\'t display timing information',
                        dest='timing', action='store_false', default=True)
    parser.add_argument('--print-AST', help='gives the AST as output',
                        dest='AST', action='store_true', default=False)
    args = parser.parse_args()

    output_str = ''
    filename = args.FILE

    if not filename.endswith('.idp'):
        raise ValueError("Expected file ending in .idp\n")
    with open(filename, 'r') as fp:
        idp_file = fp.read()

    # Perform linting.
    output_str = lint_fo(idp_file, timing=args.timing,
                         print_ast=args.AST)
    print(output_str)

if __name__ == "__main__":
    main()
