'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_member_follows = social_graph[from_member]["following"]
    to_member_follows = social_graph[to_member]["following"]
    if to_member in from_member_follows and from_member in to_member_follows:
        return ("friends")
    elif to_member in from_member_follows:
        return ("follower")
    elif from_member in to_member_follows:
        return ("followed by")
    else:
        return ("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    N = len(board)

    #1 check for winners horizontally
    for i in range (N):
        row =[]
        for j in range (N):
            row.append(board[i][j])
        if row.count(row[0]) == len (row):
                return row[0]
        
    #2 check for winners vertically
    for j in range (N):
        column =[]
        for i in range (N):
            column.append(board[i][j])
        if column.count(column[0]) == len (column):
                return column[0]
        
    #3 check for winners diagonally
    diagonal1_UL_LR = []
    for i in range (N):
        diagonal1_UL_LR.append(board[i][i])
    if diagonal1_UL_LR.count(diagonal1_UL_LR[0]) == len (diagonal1_UL_LR):
            return diagonal1_UL_LR[0]

    diagonal2_LL_UR = []
    for i in range (N):
        diagonal2_LL_UR.append(board[2-i][i])
    if diagonal2_LL_UR.count(diagonal2_LL_UR[0]) == len (diagonal2_LL_UR):
            return diagonal2_LL_UR[0]
        
    #4 If no winners return "NO WINNER"
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    route_map_list = list(route_map)
    N = len(route_map_list)
    distance = []
    
    current_stop = first_stop
    while current_stop != second_stop:
        #find the next stop
            next_stop = ""
            for i in range (N):
                if route_map_list[i][0] == current_stop:
                    next_stop = route_map_list[i][1]
    #add to the travel time distance between (current stop, next stop)
                    distance.append(route_map[route_map_list[i]]["travel_time_mins"])
                    distance
    #go to the next stop
            current_stop = next_stop
    return (sum(distance))