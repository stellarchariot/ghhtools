from team import Team
from reddit import get_reddit

def make_teams(producers, rappers):
    """
    Given a list of producers and a list of rappers, this function returns a
    list of Team objects.
    
    Constraints:
    
    - Make teams of four (two rappers and producers each) if possible
    - If there is an even number of producers but more rappers than producers:
      -- then some teams should have 3 rappers e.g. if there are 58 producers and 66 rappers, 8 teams should have 3 rappers
    - If there is an odd number of producers but more rappers than producers:
      -- then one team should have one producer and two rappers
    - If there are more producers than rappers some teams should have two producers and one rapper
    - If there is an odd and equal number of producers and rappers: one team will be one producer and one rapper
    - There should never be more than two producers or three rappers on a team
    """
    teams = []
    return teams
    
def rapper_spots_left(teams):
    total = 0
    for team in teams:
        total += team.rapper_spots_left()
    return total
        
def producer_spots_left(teams):
    total = 0
    for team in teams:
        total += team.producer_spots_left()
    return total
    
def no_of_teams_with_rappers_full(teams):
    total = 0
    for team in teams:
        if team.rapper_spots_left() == 0:
            total += 1
    return total
    
def are_teams_valid(teams):
    for team in teams:
        if not team.is_valid():
            return False
    return True
        
def get_members(url):
    reddit = get_reddit()
    
    registration_url = url
    submission = reddit.submission(url=registration_url)
    
    submission.comments.replace_more(limit=0)
    rappers = []
    producers = []
    for top_level_comment in submission.comments:
        comment_body = top_level_comment.body.lower()
        # The top level comment is usually something like 'Rapper sign up'
        # or 'Producer sign up'
        if "rapper sign" in comment_body:
            for second_level_comment in top_level_comment.replies:
                rappers.append(second_level_comment.author.name)
        elif "producer sign" in comment_body:
            for second_level_comment in top_level_comment.replies:
                producers.append(second_level_comment.author.name)
    
    # Remove duplicate usernames (e.g. if some user had double posted)
    rappers = list(set(rappers))
    producers = list(set(producers))
    
    # Shuffle them randomly
    # rappers = Random.shuffle(rappers)
    # producers = Random.shuffle(producers)
    
    return {'producers': producers, 'rappers': rappers}
    