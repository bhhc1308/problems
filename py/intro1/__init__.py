import check50

@check50.check()
def exists():
    """intro1.py exists"""
    check50.exists("intro1.py")
    check50.include("../../intro1/1.in", "../../intro1/1.out")
    check50.include("../../intro1/2.in", "../../intro1/2.out")
    check50.include("../../intro1/3.in", "../../intro1/3.out")
    check50.include("../../intro1/4.in", "../../intro1/4.out")
    check50.include("../../intro1/5.in", "../../intro1/5.out")
    check50.include("../../intro1/6.in", "../../intro1/6.out")
    check50.include("../../intro1/7.in", "../../intro1/7.out")
    check50.include("../../intro1/8.in", "../../intro1/8.out")
    check50.include("../../intro1/9.in", "../../intro1/9.out")
    check50.include("../../intro1/10.in", "../../intro1/10.out")
    check50.include("../../intro1/11.in", "../../intro1/11.out")
    check50.include("../../intro1/12.in", "../../intro1/12.out")
    check50.include("../../intro1/13.in", "../../intro1/13.out")
    check50.include("../../intro1/14.in", "../../intro1/14.out")

@check50.check(exists)
def compiles():
    """intro1.py compiles"""
    check50.run("python3 {folder_name}.py").exit(0)

@check50.check(compiles)
def demo_1():
    """demo_1"""
    test_input_output("1.in", "1.out")

@check50.check(compiles)
def demo_2():
    """demo_2"""
    test_input_output("2.in", "2.out")

@check50.check(compiles)
def demo_3():
    """demo_3"""
    test_input_output("3.in", "3.out")

@check50.check(compiles)
def demo_4():
    """demo_4"""
    test_input_output("4.in", "4.out")

@check50.check(compiles)
def demo_5():
    """demo_5"""
    test_input_output("5.in", "5.out")

@check50.check(compiles)
def demo_6():
    """demo_6"""
    test_input_output("6.in", "6.out")

@check50.check(compiles)
def demo_7():
    """demo_7"""
    test_input_output("7.in", "7.out")

@check50.check(compiles)
def demo_8():
    """demo_8"""
    test_input_output("8.in", "8.out")

@check50.check(compiles)
def demo_9():
    """demo_9"""
    test_input_output("9.in", "9.out")

@check50.check(compiles)
def demo_10():
    """demo_10"""
    test_input_output("10.in", "10.out")

@check50.check(compiles)
def demo_11():
    """demo_11"""
    test_input_output("11.in", "11.out")

@check50.check(compiles)
def demo_12():
    """demo_12"""
    test_input_output("12.in", "12.out")

@check50.check(compiles)
def demo_13():
    """demo_13"""
    test_input_output("13.in", "13.out")

@check50.check(compiles)
def demo_14():
    """demo_14"""
    test_input_output("14.in", "14.out")

# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 {folder_name}.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
