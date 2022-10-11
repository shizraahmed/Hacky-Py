from assertpy import assert_that

# Your job is to write a function which increments a string,
#  to create a new string.

# If the string already ends with a number,
#  the number should be incremented by 1.
# If the string does not end with a number.
#  the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount
#  of digits should be considered.

def increment_the_end_number_by_one(line: str) -> str:
    head = line.rstrip('0123456789')
    tail = line[len(head):]
    if tail == "":
        return line + "1"
    return head + str(int(tail) + 1).zfill(len(tail))

class TestIncrementalString:
    def test_increments_without_number_at_the_end(self):
        assert_that(increment_the_end_number_by_one("foo")).is_equal_to("foo1")
        assert_that(increment_the_end_number_by_one("")).is_equal_to("1")

    def test_increments_number(self):
        assert_that(increment_the_end_number_by_one("foobar23")).is_equal_to("foobar24")

    def test_increments_number_keeping_zeros(self):
        assert_that(increment_the_end_number_by_one("foo0042")).is_equal_to("foo0043")

    def test_increments_number_adding_one_digit_for_multiples_of_ten(self):
        assert_that(increment_the_end_number_by_one("foo9")).is_equal_to("foo10")

    def test_increments_number_changing_previous_zero_for_multiples_of_ten(self):
        assert_that(increment_the_end_number_by_one("foo099")).is_equal_to("foo100")

    def test_increments_number_with_interpolated_numbers(self):
        assert_that(increment_the_end_number_by_one("1fo2o")).is_equal_to("1fo2o1")
        assert_that(increment_the_end_number_by_one("1fo2o099")).is_equal_to("1fo2o100")
