from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Queue, Stack

import multiprocessing

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#define a traverse maze method
def travers_maze(test=True):
    #this is the final path
    final_path = []
    # revers of traversal_path
    reversed_path = []
    # visited
    visited = {}
    #dict to get opposite direction travelled
    from_dir = {"n": "s", "s": "n", "w": "e", "e": "w"}
    #Building starting room and exits
    visited[player.current_room.id] = player.current_room.get_exits()

    #run until all rooms have been visited
    while len(visited)< len(room_graph)-1:
        #if unvisited
        if player.current_room.id not in visited:
            #add current room player is in to visited
            visited[player.append(current_room.id)]
            #get the room exits
            player.current_room.get_exits()
            #add room and exits to visited
            visited[player.current_room.id].remove(revesed_path[-1])
        else:
            if len(visited)> 1:
                visited[player.current_room.id].remove(revesed_path[-1])
        # need to back track to a previous room
        if len(visited[player.current_room.id]) == 0:
            #while statements to verify length of the room
            while len(visited[player.current_room.id]) == 0:
                #to go back to a previous room
                go_back_a_room = reversed_path.pop()
                #add to the path 
                final_path.append(go_back_a_room)
                #move the player to the previous room
                player.travel(go_back_a_room)
        else:
            #pick last available direction
            direction = visited[player.current.id].pop()
            #move player
            player.travel(direction)
            #append to final path
            final_path.append(direction)
            #add direction to traversal path
            reversed_path.append(from_dir[direction])

    return final_path

def traversal_test():
    # TRAVERSAL TEST
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)

    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)

    if len(visited_rooms) == len(room_graph):
        print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

