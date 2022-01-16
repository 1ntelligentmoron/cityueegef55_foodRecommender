def recommend(budget, range, lat, long):
    r1 = 'Lam Cheong Kee'
    r2 = 'Pot & Plate'
    r3 = 'Pacific Coffee Company'
    kw1 = ('Hong Kong Style', 'Snack Shop & Deli')
    kw2 = ('Taiwan', 'Japanese')
    kw3 = ('Western', 'Salad')
    addr1 = 'Shop 108A, 1/F, New East Ocean Centre, 9 Science Museum Road, Tsim Sha Tsui'
    addr2 = 'Shop 756, 7/F, Fortune Metropolis, 6-10 Metropolis Drive, Hung Hom'
    addr3 = 'Podium, Pao Yue-kong Library, The Hong Kong Polytechnic University, Hung Hom'
    coord1 = (22.3015905, 114.1790255)
    coord2 = (22.302663, 114.183191)
    coord3 = (22.302516, 114.178928)
    r_id1 = 4581
    r_id2 = 6594
    r_id3 = 4087
    return ((r1, kw1, addr1, coord1, r_id1), (r2, kw2, addr2, coord2, r_id2), (r3, kw3, addr3, coord3, r_id3))

def chosen(r_id):
    return 'You have chosen restaurant ID#{}.'.format(r_id)
