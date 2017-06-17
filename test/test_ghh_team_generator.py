import unittest
import ghhtools.ghh_team_generator as ghh
from ghhtools.team import Team
from ghhtools.ghh_input_error import GHHInputError

class GHHTeamGeneratorTestCase(unittest.TestCase):
    def test_even_and_equal(self):
        teams = ghh.make_teams(['AVerma', 'letsruntrack', 'tino', 'kypsa'], ['stellarchariot', 'ADPMC', 'jeff', 'xagee_flame'])
        team_1 = Team()
        team_1.add_producers(['AVerma', 'letsruntrack'])
        team_1.add_rappers(['stellarchariot', 'ADPMC'])
        team_2 = Team()
        team_2.add_producers(['tino', 'kypsa'])
        team_2.add_rappers(['jeff', 'xagee_flame'])
        self.assertEqual(teams, [team_1, team_2])
        
    def test_odd_and_equal(self):
        teams = ghh.make_teams(['AVerma', 'letsruntrack', 'tino', 'kypsa', 'yukari'], ['stellarchariot', 'ADPMC', 'jeff', 'xagee_flame', 'reeg'])
        team_1 = Team()
        team_1.add_producers(['AVerma', 'letsruntrack'])
        team_1.add_rappers(['stellarchariot', 'ADPMC'])
        team_2 = Team()
        team_2.add_producers(['tino', 'kypsa'])
        team_2.add_rappers(['jeff', 'xagee_flame'])
        team_3 = Team()
        team_3.add_producers(['yukari'])
        team_3.add_rappers(['reeg'])
        self.assertEqual(teams, [team_1, team_2, team_3])
        
    def test_one_and_equal(self):
        teams = ghh.make_teams(['AVerma'], ['stellarchariot'])
        team_1 = Team()
        team_1.add_producers(['AVerma'])
        team_1.add_rappers(['stellarchariot'])
        self.assertEqual(teams, [team_1])
        
    def test_none_and_equal(self):
        teams = ghh.make_teams([], [])
        self.assertEqual(teams, [])
        
    def test_more_rappers_than_producers(self):
        teams = ghh.make_teams(['AVerma', 'letsruntrack', 'tino'], ['stellarchariot', 'ADPMC', 'jeff', 'xagee_flame', 'reeg'])
        team_1 = Team()
        team_1.add_producers(['AVerma', 'letsruntrack'])
        team_1.add_rappers(['stellarchariot', 'ADPMC', 'xagee_flame'])
        team_2 = Team()
        team_2.add_producers(['tino'])
        team_2.add_rappers(['jeff', 'reeg'])
        self.assertEqual(teams, [team_1, team_2])
        
    def test_more_producers_than_rappers(self):
        teams = ghh.make_teams(['AVerma', 'letsruntrack', 'tino', 'IbrahimT13', 'Alliswell'], ['stellarchariot', 'ADPMC', 'jeff', 'xagee_flame'])
        team_1 = Team()
        team_1.add_producers(['AVerma', 'letsruntrack'])
        team_1.add_rappers(['stellarchariot', 'ADPMC'])
        team_2 = Team()
        team_2.add_producers(['tino', 'IbrahimT13'])
        team_2.add_rappers(['jeff', 'xagee_flame'])
        team_3 = Team()
        team_3.add_producers(['Alliswell'])
        team_3.add_rappers(['reeg'])
        self.assertEqual(teams, [team_1, team_2, team_3])
        
    def test_way_more_rappers_than_producers(self):
        with self.assertRaises(GHHInputError) as context:
            teams = ghh.make_teams(['AVerma', 'letsruntrack', 'tino'], ['stellarchariot', 'ADPMC', 'jeff', 'xagee_flame', 'reeg', 'eminem', 'slug', 'lupe', 'nas', 'jay_z', 'drake', 'aesop_rock', 'oddisee', 'briggs', '@peace'])
        error_msg = context.exception.message
        self.assertTrue('There are too many rappers' in error_msg)
        
    def test_way_more_producers_than_rappers(self):
        with self.assertRaises(GHHInputError) as context:
            teams = ghh.make_teams(['AVerma', 'letsruntrack', 'tino', 'IbrahimT13', 'Alliswell', 'Pittsoul', 'js_beats', 'NoiseWitch', 'NewGates', 'stod', 'oysta'], ['stellarchariot', 'ADPMC', 'jeff'])
        error_msg = context.exception.message
        self.assertTrue('There are too many producers' in error_msg)

if __name__ == '__main__':
    unittest.main()