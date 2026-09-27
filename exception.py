# number = 10
# # if number > 5:
# #     raise Exception(f"The number should not exceed 5. {num}")
# assert (number < 5), f"The number should not exceed 5. ({number=})"
# print(number)
import sys
def linux_interaction():
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

if __name__ == '__main__':
    try:
        linux_interaction()
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print('fnf_error : ',fnf_error)
    except RuntimeError as error:
        print('error : ',error)
        print("Linux linux_interaction() function wasn't executed.")
    # try:
    #     linux_interaction()
    # except RuntimeError as error:
    #     print(error)
    # else:
    #     print('Doing even more Linux things.')
