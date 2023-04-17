def sainte_lague(votes, seats):
    party_seats = [0] * len(votes)
    divisors = [1 / (2 * i + 1) for i in range(seats)]

    for _ in range(seats):
        max_value = -1
        max_index = -1

        for i, votes_for_party in enumerate(votes):
            temp_value = votes_for_party / divisors[party_seats[i]]
            if temp_value > max_value:
                max_value = temp_value
                max_index = i

        party_seats[max_index] += 1

    return party_seats
  
def hare_niemeyer(votes, seats):
    total_votes = sum(votes)
    quotas = [votes_for_party / total_votes * seats for votes_for_party in votes]
    party_seats = [int(quota) for quota in quotas]

    remaining_seats = seats - sum(party_seats)
    remainders = [quota - int(quota) for quota in quotas]

    for _ in range(remaining_seats):
        max_remainder_index = remainders.index(max(remainders))
        party_seats[max_remainder_index] += 1
        remainders[max_remainder_index] = 0

    return party_seats

def dhondt(votes, seats):
    party_seats = [0] * len(votes)
    divisors = [i + 1 for i in range(seats)]

    for _ in range(seats):
        max_value = -1
        max_index = -1

        for i, votes_for_party in enumerate(votes):
            temp_value = votes_for_party / divisors[party_seats[i]]
            if temp_value > max_value:
                max_value = temp_value
                max_index = i

        party_seats[max_index] += 1

    return party_seats.
  
votes = [100, 80, 70, 50]
seats = 10

sainte_lague_result = sainte_lague(votes, seats)
hare_niemeyer_result = hare_niemeyer(votes, seats)
dhondt_result = dhondt(votes, seats)

print(f"Sainte-Lague: {sainte_lague_result}")
print(f"Hare-Niemeyer: {hare_niemeyer_result}")
print(f"D'Hondt: {dhondt_result}")
input()
