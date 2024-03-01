import logic
import utils


def printMenu():
    '''
    :return: Displays the menu
    '''

    msg = "Menu: \n"
    msg += "\t *. Read the list \n"
    msg += "\t **. Display the list \n"
    msg += "\t 1. Add value as last element of array \n"
    msg += "\t 2. Insert number value at index \n"
    msg += "\t 3. Removes the element at index \n"
    msg += "\t 4. Removes elements between the two given index \n"
    msg += "\t 5. Replaces the score on index with new_value \n"
    msg += "\t 6. Get participants with score less than value \n"
    msg += "\t 7. Get all participants sorted by their score \n"
    msg += "\t 8. Get the participants with scores higher than value sorted \n"
    msg += "\t 9. Get the average score for participants between the two given index \n"
    msg += "\t 10. Get the minimum score for participants 1..5 \n"
    msg += "\t 11. Get the score of participants between the two given index, which are multiples of value \n"
    msg += "\t 12. Get the score of participants 1...5, which are multiples of 10 \n"
    msg += "\t 13. Keep only participants with scores multiple of value, removing the other participants(scores) \n"
    msg += "\t 14. Keep onlt participants with scores higher than value,removing the other participants(scores) \n"
    msg += "\t 0. Exit \n"
    print(msg)


def main():
    """
    :return: Starts the application
    """

    score_list = []
    undo_list = []
    printMenu()
    stop = False
    while not stop:
        command = int(input("Enter option: "))
        if command == 100:
            utils.readList(score_list)
        elif command ==101:
            print(score_list)

        elif command == 1:
            undo_list.append(score_list[:])
            value = int(input("Enter the value to be added to the list: "))
            print("The list after adding a new value is:",
                  logic.add(score_list, value))
        elif command == 2:
            undo_list.append(score_list[:])
            index = int(input("Enter the index where you want to add an element: "))
            value = int(input("Enter the value you want to add in the list: "))
            print("The list after adding a new value on a given index is:",
                  logic.insert(score_list,index, value))
        elif command == 3:
            undo_list.append(score_list[:])
            index = int(input("Enter the index of the element to be removed from the list: "))
            print("The list after removing the element from a given index:",
                  logic.remove(score_list, index))
        elif command == 4:
            undo_list.append(score_list[:])
            from_index = int(input("Enter the first index of the interval: "))
            to_index = int(input("Enter the last index of the interval: "))
            print("The list after removing the numbers between the given indices is:",
                  logic.remove2(score_list, from_index, to_index))
        elif command == 5:
            undo_list.append(score_list[:])
            index = int(input("Enter the index of the element that will be replaced: "))
            new_value = int(input("Enter the value to replace the old one: "))
            print("The list after replaceing with the new value is:",logic.replace(score_list, index, new_value))
        elif command == 6:
            value = int(input("Enter the value: "))
            print("The list of participants with score less than value", logic.less(score_list, value))
        elif command == 7:
            print("List of participants sorted by their score", logic.sorted(score_list))
        elif command == 8:
            value = int(input("Enter the value: "))
            print("The list of participants with the score higher than value sorted is: ", logic.sorted2(score_list, value))
        elif command == 9:
            from_index = int(input("Enter the first index of the interval: "))
            to_index = int(input("Enter the last index of the interval: "))
            print("The average score for participants betwen indexes:",
                  logic.avg(score_list, from_index, to_index))
        elif command == 10:
            from_index = int(input("Enter the first index of the interval: "))
            to_index = int(input("Enter the last index of the interval: "))
            print("The minimum value between the given indexes is", logic.min(score_list, from_index, to_index))
        elif command == 11:
            value = int(input("Enter the value: "))
            from_index = int(input("Enter the first index of the interval: "))
            to_index = int(input("Enter the last index of the interval: "))
            print("The score of participants between indexes is: ", logic.mul(score_list,value,from_index, to_index))
        elif command == 12:
            undo_list.append(score_list[:])
            value = int(input("Enter the value: "))
            print("The filtered list is", logic.filter_mul(score_list,value))
        elif command == 13:
            undo_list.append(score_list[:])
            value = int(input("Enter the value: "))
            print("The filtered list is", logic.filter_mul(score_list, value))
        elif command == 14:

            print("The last operation was eliminated:", logic.undo(undo_list))

        elif command == 0:
            print("Goodbye")
            stop = True
        else:
            print("Invalid option")