def encrypt_file(input_filename, output_filename):
    with open(input_filename, 'rb') as input_file:
        with open(output_filename, 'wb') as output_file:
            byte = input_file.read(1)
            while byte:
                encrypted_byte = bytes([(byte[0] + 5) % 256])
                output_file.write(encrypted_byte)
                byte = input_file.read(1)

def decrypt_file(input_filename, output_filename):
    with open(input_filename, 'rb') as input_file:
        with open(output_filename, 'wb') as output_file:
            byte = input_file.read(1)
            while byte:
                decrypted_byte = bytes([(byte[0] - 5) % 256])
                output_file.write(decrypted_byte)
                byte = input_file.read(1)
                
def main():
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    input_filename = input("Enter input filename: ")
    output_filename = input("Enter output filename: ")

    if choice == 'E':
        encrypt_file(input_filename, output_filename)
        print("File encrypted successfully.")
    elif choice == 'D':
        decrypt_file(input_filename, output_filename)
        print("File decrypted successfully.")
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

    # Print content of encrypted or decrypted files
    with open(output_filename, 'rb') as file:
        print(f"Content of {output_filename}:")
        print(file.read().decode())

if __name__ == "__main__":
    main()
