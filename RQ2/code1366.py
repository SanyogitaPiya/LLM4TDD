from typing import List
import unittest

class Solution:
    def code1366(self, votes: List[str]) -> str:
        # Handle the case with the minimum input values
        if len(votes) == 1:
            return votes[0]

        # Create a dictionary to store votes for each team and each rank
        vote_count = {}

        for vote in votes:
            for i, team in enumerate(vote):
                if team not in vote_count:
                    vote_count[team] = [0] * len(vote)
                vote_count[team][i] += 1

        # Sort the teams based on vote count for the first rank and team IDs
        sorted_teams = sorted(vote_count.keys(), key=lambda x: vote_count[x], reverse=True)
        teams = sorted(sorted_teams, key=lambda x: vote_count[x][0], reverse=True)

        return ''.join(teams)
