def feedDog(hunger_level, biscuit_size):
    hunger_level.sort(reverse=True)
    biscuit_size.sort()
    output = 0
    for hunger in hunger_level:
        for biscuit in biscuit_size:
            if hunger <= biscuit:
                biscuit_size.pop()
                output += 1
                break
    return output

