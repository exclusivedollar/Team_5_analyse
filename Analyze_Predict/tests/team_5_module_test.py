from Analyze_Predict import team_5_module

def test_date_parser():

    """
    Make sure date_parser works correctly

    """

assert team_5_module.date_parser([
    '2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10'
]) == ['2019-11-20', '2019-11-20', '2019-11-20'], 'incorrect'