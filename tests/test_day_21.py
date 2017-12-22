
from .. import day_21
RULES = day_21.get_rules(filename='day_21_alt.txt')

def test_swizzle_of_threes_for_prep():
    # rules = day_21.get_rules()
    key = '#../#.#/..#/#../#.#/..#/#../#.#/..#/.../.##/###'
    parsed = day_21.parse_pattern(key)
    assert key == parsed

    groups = parsed.split('/')
    print([groups[index:index+3] for index in range(0, len(groups), 3)])
    result = list()
    for item in day_21.yield_swizzle_pattern(parsed):
        result.append(item)
    assert '#../#../..#/#.#/#../..#/#.#/.../..#/#.#/.##/###' == '/'.join(result)


def test_apply_3x3_to_2x2_key():
    key = '.#...####'
    parsed = day_21.parse_pattern(key)
    result = day_21.get_new_pattern(parsed, RULES)
    assert '#..#/..../..../#..#' == result


def test_applly_3x3_to_2x2_key_w_enhancement_rules():
    key = '.#...####'
    result = day_21.apply_enhancement_rules(key, RULES)
    assert '#..#/..../..../#..#' == result


def test_apply_2x2_to_3x3_key_w_enhancement_rules():
    key = '#..#/..../..../#..#'
    result = day_21.apply_enhancement_rules(key, RULES)
    assert '##./#../.../##./#../.../##./#../.../##./#../...' == result


def test_parse_key_from_fours_to_twos():
    key = '#..#/....'
    result = day_21.parse_pattern(key)
    assert '#./.#/../..' == result


def test_parse_key_from_fours_to_twos_b():
    key = '#..#/..../..../#..#'
    result = day_21.parse_pattern(key)
    assert '#./.#/../../../../#./.#' == result


def test_parse_key_from_twos_to_twos():
    key = '.#/##/##/#./../##/##/#.'
    result = day_21.parse_pattern(key)
    assert '.#/##/##/#./../##/##/#.' == result


def test_parse_key_from_threes_to_threes():
    key = '##./#../.../##./#../...'
    result = day_21.parse_pattern(key)
    assert '##./#../.../##./#../...' == result


def test_parse_key_from_sixes_to_twos():
    key = '##.#../...##./#.....'
    result = day_21.parse_pattern(key)
    assert '##/.#/../../.#/#./#./../..' == result
