import check50

@check50.check()
def exists():
    """demo.java exists"""
    check50.exists("Demo.java")
    check50.include("../../demo/Ram_input.txt", "../../demo/Ram_output.txt")
    check50.include("../../demo/Charan_input.txt", "../../demo/Charan_output.txt")

@check50.check(exists)
def compiles():
    """demo.java compiles"""
    check50.run("javac Demo.java").exit(0)


@check50.check(compiles)
def demo_2_3():
    """demo_Ram"""
    test_input_output("Ram_input.txt", "Ram_output.txt")


@check50.check(compiles)
def demo_20_22():
    """demo_Charan"""
    test_input_output("Charan_input.txt", "Charan_output.txt")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "java Demo"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
