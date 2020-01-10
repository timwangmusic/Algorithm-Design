from typing import List
from pprint import pprint as pp


class Place:
    def __init__(self, name: str, score: float, time_needed: int, cost: int):
        self.name = name
        self.score = score
        self.time_needed = time_needed
        self.cost = cost


class Result:
    def __init__(self):
        self.score = 0.0
        self.places = []


def dp(time_allowance: int, budget: int, idx: int, places: List[Place], memo: dict) -> Result:
    if (time_allowance, budget, idx) not in memo:
        memo[time_allowance, budget, idx] = Result()
        if idx >= 0 and time_allowance > 0 and budget > 0:
            place = places[idx]
            if place.cost <= budget and place.time_needed <= time_allowance:
                prev_res_same_budget = dp(time_allowance, budget, idx - 1, places, memo)
                prev_res = dp(time_allowance - place.time_needed, budget - place.cost, idx - 1, places, memo)
                if prev_res.score + place.score >= prev_res_same_budget.score:
                    new_result = Result()
                    new_result.places = list(prev_res.places) + [place]  # copy places list
                    new_result.score = prev_res.score + place.score
                    memo[time_allowance, budget, idx] = new_result
                else:
                    memo[time_allowance, budget, idx] = dp(time_allowance, budget, idx - 1, places, memo)
            else:
                memo[time_allowance, budget, idx] = dp(time_allowance, budget, idx - 1, places, memo)
    return memo[time_allowance, budget, idx]


def multiDimensionalKnapsack(total_time: int, budget: int, places: List[Place]) -> Result:
    memo = {}
    dp(total_time, budget, len(places)-1, places, memo)
    return memo[total_time, budget, len(places)-1]


if __name__ == "__main__":
    place_a = Place("A", 4.0, 1, 2)
    place_b = Place("B", 3.5, 2, 1)
    place_c = Place("C", 5.0, 2, 1)
    res = multiDimensionalKnapsack(2, 1, [place_a, place_b, place_c])
    pp(res.score)
    pp([place.name for place in res.places])
