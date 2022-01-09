def recommend(budget, range, lat, long):
    r1 = '[Restaurant 1]'
    r2 = '[Restaurant 2]'
    r3 = '[Restaurant 3]'
    kw1 = ('[A1]', '[B1]')
    kw2 = ('[A2]', '[B2]')
    kw3 = ('[A3]', '[B3]')
    addr1 = '[Address 1]'
    addr2 = '[Address 2]'
    addr3 = '[Address 3]'
    coord1 = (0.0, 0.0)
    coord2 = (0.0, 0.0)
    coord3 = (0.0, 0.0)
    r_id1 = 1
    r_id2 = 2
    r_id3 = 3
    return ((r1, kw1, addr1, coord1, r_id1), (r2, kw2, addr2, coord2, r_id2), (r3, kw3, addr3, coord3, r_id3))

def chosen(r_id):
    return 'You have chosen restaurant ID#{}.'.format(r_id)
