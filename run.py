situation = 'start'


while True:
    main.choice = ''
    system(main.clcmd)
    cur_situation = getattr(main, situation)
    cur_situation()
    situation = main.next_situation
