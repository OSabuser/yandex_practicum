from sprint_2.t6_stack_max_effective.solution import Stack


def test_get_stacks_max_item_value():
    user_stack = Stack()
    user_stack.push(-11)
    user_stack.push(0)
    user_stack.push(11)
    assert user_stack.get_max() == 11


def test_pop_item_from_empty_stack():
    user_stack = Stack()
    assert user_stack.pop() == "error"


def test_get_stacks_max_item_value_from_empty_stack():
    user_stack = Stack()
    assert user_stack.get_max() == "None"


def test_custom_workflow():
    user_stack = Stack()
    user_stack.push(1)
    user_stack.push(-4444)
    user_stack.push(3)
    user_stack.push(2)
    user_stack.push(5)
    assert user_stack.get_max() == 5
    assert user_stack.pop() == 5
    assert user_stack.get_max() == 3
    assert user_stack.pop() == 2
    assert user_stack.pop() == 3
    assert user_stack.get_max() == 1
    assert user_stack.pop() == -4444
    assert user_stack.pop() == 1
    assert user_stack.pop() == "error"
    assert user_stack.get_max() == "None"


def test_custom_workflow_2():
    user_stack = Stack()
    user_stack.push(1)
    user_stack.push(-4444)
    assert user_stack.top() == -4444
    user_stack.push(3)
    user_stack.push(2)
    user_stack.push(5)
    assert user_stack.get_max() == 5
    assert user_stack.pop() == 5
    assert user_stack.top() == 2
    assert user_stack.get_max() == 3
    assert user_stack.pop() == 2
    assert user_stack.top() == 3
    assert user_stack.pop() == 3
    assert user_stack.top() == -4444
    assert user_stack.get_max() == 1
    assert user_stack.pop() == -4444
    assert user_stack.pop() == 1
    assert user_stack.pop() == "error"
    assert user_stack.get_max() == "None"
    assert user_stack.top() == "error"
