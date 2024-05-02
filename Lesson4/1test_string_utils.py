import pytest 
from string_utils import StringUtils

string_utils = StringUtils()

# тест 1
@pytest.mark.parametrize('param, result',[
    ('sorokina', 'Sorokina'),
    ('Mariya', 'Mariya'),
    ('paRametr', 'Parametr'),
    ('first test', 'First test'),    
    ('piter Parker', 'Piter parker')
])
def test_positive_capitalize(param, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(param)
    assert res == result

@pytest.mark.parametrize('param, result', [
    ('Piter', 'Piter'),
    ('SMS', 'Sms'),
    ('', ''),
    ('123', '123'),
    (' ', ' '),    
    ('123qwe', '123qwe'),
    ('qwe123', 'Qwe123'),
])
def test_negative_capitalize(param, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(param)
    assert res == result

# тест 2
@pytest.mark.parametrize('param, result', [
    (' Mariya', 'Mariya'),
    ('Mariya', 'Mariya'),
    (' test', 'test'),
    (' test test', 'test test'),
    (' test ', 'test '),
    ('test ', 'test ')
])
def test_positive_trim(param, result):
    string_utils = StringUtils()
    res = string_utils.trim(param)
    assert res == result

@pytest.mark.parametrize('param, result', [
    (' ', ''),
    ('te st', 'te st'),
    ('123', '123')
])
def test_negative_trim(param, result):
    string_utils = StringUtils()
    res = string_utils.trim(param)
    assert res == result

# тест 3
@pytest.mark.parametrize('param, dilimeter, result', [
    ('one,two,three', ',', ['one', 'two', 'three']),
    ('1:2:3:4', ':', ['1', '2', '3', '4']),
    ])

def test_positive_to_list(param, dilimeter, result):
    if dilimeter is None:
        res = string_utils.to_list(param)
    else:
        res = string_utils.to_list(param, dilimeter)

    assert res == result

@pytest.mark.parametrize('param, dilimeter, result', [
    ('', None, []),
    ('1,2,3,4 5', None, ['1', '2', '3', '4 5']),
    ])

def test_negative_to_list(param, dilimeter, result):
    if dilimeter is None:
        res = string_utils.to_list(param)
    else:
        res = string_utils.to_list(param, dilimeter)

    assert res == result

# тест 4
@pytest.mark.parametrize('param, simbol, result', [
    ('Test', 'T', True),
    ('test', 't', True),
    ('test-test', '-', True),
    ('123', '1', True),
    ('SMS', 'S', True),
    ('', '', True),
    (' qwe', ' ', True),
    ('true ', 't', True)
])

def test_positive_contains(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(param, simbol)
    assert res == result

@pytest.mark.parametrize('param, simbol, result', [
    ('Test', 'o', False),
    ('Queen', 'q', False),
    ('123', '!', False),
    ('', '1', False)
])

def test_negative_contains(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(param, simbol)
    assert res == result

# тест 5
@pytest.mark.parametrize('param, simbol,result', [
    ('library', 'lib', 'rary'),
    ('Test-Test', '-', 'TestTest'),
    ('Anna Mariya', ' ', 'AnnaMariya'),
    ('window in Europe', 'in', 'wdow  Europe'),
    ('123 + 123', '+', '123  123'),
    ('Moscow', 'M', 'oscow'),
    ('Sun', 'n', 'Su')
])

def test_positive_delete_simbol(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(param, simbol)
    assert res == result

@pytest.mark.parametrize('param, simbol,result', [
    ('library', '', 'library'),
    ('TestTest', '-', 'TestTest'),
    ('Anna Mariya', '-', 'Anna Mariya'),
    ('', '', ''),
    ('', '+', ''),
])

def test_negative_delete_simbol(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(param, simbol)
    assert res == result

# тест 6
@pytest.mark.parametrize('param, simbol, result', [
    ('Moscow', 'M', True),
    ('test', 't', True),
    (' test', ' ', True),
    ('1234qwe', '1', True),
    ('qwe123', 'q',True),
    ('!Hello', '!', True)
])

def test_positive_starts_with(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(param, simbol)
    assert res == result

@pytest.mark.parametrize('param, simbol, result', [
    ('Moscow', 'm', False),
    ('test', 'T', False),
    (' test', 't', False),
    ('1234qwe', '2', False),
    ('qwe123', '1',False),
    ('!Hello', 'H', False),
    (' Hello', 'H', False),
    ('Test', ' ', False)
])

def test_negative_starts_with(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(param, simbol)
    assert res == result

# тест 7
@ pytest.mark.parametrize('param, simbol, result', [
    ('Test', 't', True),
    ('marY', 'Y', True),
    ('No-', '-', True),
    ('qw13', '3', True),
    ('32we', 'e', True),
    ('123', '3', True),
    ('call ', ' ', True)
])

def test_positive_end_with(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(param, simbol)
    assert res == result

@ pytest.mark.parametrize('param, simbol, result', [
    ('Test', 'T', False),
    ('marY', 'm', False),
    ('No-', ' ', False),
    ('qw13', 'q', False),
    ('32we', 'w', False),
    ('123', '2', False),
    ('call ', 'l', False)
])

def test_negative_end_with(param, simbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(param, simbol)
    assert res == result

# тест 8
@pytest.mark.parametrize('param, result', [
    ('', True),
    ('    ', True),
    (' ', True)
])

def test_positive_is_empty(param, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(param)
    assert res == result

@pytest.mark.parametrize('param, result', [
    ('q', False),
    (' 1', False),
    ('1 ', False),
    ('test', False)
])

def test_negative_is_empty(param, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(param)
    assert res == result

# тест 9
@pytest.mark.parametrize('lst, joiner, result', [
    (['one', 'two', 'three'], ',', 'one,two,three'),
    ([1,2,3,4,5], None, '1, 2, 3, 4, 5'),
    (['test', 'Test'], '', 'testTest'),
    (['Test', 'Test'], '-', 'Test-Test')
])

def test_positive_list_to_string(lst, joiner, result):
    string_utils = StringUtils()
    if joiner == None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)

    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [
    ([], ',', ''),
    ([], None, '')
])

def test_negative_list_to_string(lst, joiner, result):
    string_utils = StringUtils()
    if joiner == None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)

    assert res == result