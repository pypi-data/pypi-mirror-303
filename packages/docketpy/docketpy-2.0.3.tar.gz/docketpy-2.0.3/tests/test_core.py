from docketpy.core import Person, Student

def test_person():
    p = Person('John Doe', 25)
    assert p.name == 'John Doe'

def test_student():
    s = Student('John Doe', 25, 'MIT')
    assert s.name == 'John Doe'
    assert s.get_age() == 25
    assert s.get_school() == 'MIT'
