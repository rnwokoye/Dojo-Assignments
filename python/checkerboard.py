for i in range(0,20):
    if i % 2 == 0:
        if i < 10:
            print '* ' * 10
        elif i > 10:
            print '- ' * 10
    else:
        if i > 10:
            print '- ' * 10
        elif i < 10:
            print ' *' * 10



