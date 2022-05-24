from main import leep_year


def test_case_1_leep_year():

    assert leep_year(2000) == True


def test_case_2_leep_year():

    assert leep_year(2100) == False


def test_case_3_leep_year():

    assert leep_year(1992) == True


def test_case_4_leep_year():

    assert leep_year(1900) == False


def test_case_5_leep_year():

    years = [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]
    a = [False, False, False, False, False, False, False, False]
    b = []

    for year in years:
        b.append(leep_year(year))
    assert b == a


def test_case_6_leep_year():

    years = [1600, 2000, 2400]
    a = [True, True, True]
    b = []

    for year in years:
        b.append(leep_year(year))
    assert b == a


def test_case_7_leep_year():

    years = [1988, 1992, 1996]
    a = [True, True, True]
    b = []

    for year in years:
        b.append(leep_year(year))
    assert b == a
