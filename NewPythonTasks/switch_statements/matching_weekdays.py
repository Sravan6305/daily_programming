def is_weekend(num):
    match num:
        case 1:
            return 'monday'
        case 2:
            return 'tuesday'
        case 3:
            return 'wednesday'
        case 4:
            return 'thursday'
        case 5:
            return 'friday'
        case 6:
            return 'saturday'
        case 7:
            return 'sunday'
        case _:
            return 'invalid day'

print(is_weekend(2))
print('wow what a beauty')