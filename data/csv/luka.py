
#works up until the games he sat (load management BUM)
with open('2022-2023.csv', 'r') as file:
    for line in file:
    #contents = file.read()
    #print(contents)
        data = line.strip().split(',')
        #people don't even look at half of these stats(I don't either)
       
        if data[0].isdigit():
            print(data)
        else:
            print("Skipping line:", line)
        
        # assigning data types and whatnot
        rank = int(data[0])
        season_game = int(data[1])
        age = data[3]
        team = data[4]
        opponent = data[6]
        games_started = int(data[8])
        minutes = data[9]
        fg = int(data[10])
        fg_attempted = int(data[11])
        fg_percentage = float(data[12])
        three_point = int(data[13])
        three_point_attempted = int(data[14])
        three_point_percentage = float(data[15])
        ft = int(data[16])
        ft_attempted = int(data[17])
        ft_percentage = float(data[18])
        o_rebound = int(data[19])
        d_rebound = int(data[20])
        total_rebound = int(data[21])
        asts = int(data[22])
        stls = int(data[23])
        blks = int(data[24])
        tov = int(data[25])
        fouls = int(data[26])
        points = int(data[27])
        game_score = float(data[28])
        plus_minus = int(data[29])
        
        # print values to test
        print("Rank:", rank)
        print("Season Game:", season_game)
        print("Age(Year-Day):", age)
        print("Team:", team)
        print("Opponent:", opponent)
        print("Games Started:", games_started)
        print("Minutes:", minutes)
        print("FG:", fg)
        print("FG Attempted:", fg_attempted)
        print("FG Percentage:", fg_percentage)
        print("3P:", three_point)
        print("3P Attempted:", three_point_attempted)
        print("3P Percentage:", three_point_percentage)
        print("FT:", ft)
        print("FT Attempted:", ft_attempted)
        print("FT Percentage:", ft_percentage)
        print("O Rebound:", o_rebound)
        print("D Rebound:", d_rebound)
        print("Total Rebound:", total_rebound)
        print("AST:", asts)
        print("STL:", stls)
        print("BLK:", blks)
        print("TOV:", tov)
        print("Fouls:", fouls)
        print("Points:", points)
        print("Game Score:", game_score)
        print("Plus/Minus:", plus_minus)
        print(" ")#newline to make stats more readable
        print(" ")#^^^
