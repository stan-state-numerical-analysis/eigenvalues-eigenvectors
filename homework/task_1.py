# Task: Introduction to Eigenvalues and Eigenvectors

# 1. Import numpy with its corresponding alias.



# 2. Initialize a square matrix A to be the following:
# | 4 3 |
# | 1 3 |



# 3. Use the np.linalg.eig function to calculate the eigenvalues and eigenvectors of A.
#    - Save the eigenvalues in a variable called eigenvalues.
#    - Save the eigenvectors in a variable called eigenvectors.



# 4. Print:
# Eigenvalues: ###
# where ### are the eigenvalues from above.



# 5. Print:
# Eigenvectors: ###
# where ### are the eigenvectors from above.



# 6. Create a function called check_eigensystem that verifies whether a set of vectors and a set of eigenvalues
# represents the eigensystem of A.
#    - Parameters:
#      - A: The matrix for which the eigenvector is being checked.
#      - eigenvalues: The corresponding list of eigenvalues.
#      - eigenvectors: The list of vectors being tested as eigenvectors.



    # 7. Use a loop and the zip function to iterate through each eigenvalue-eigenvector pair.



        # 8. Use numpy's allclose comparison operator to check if the pair
        # is indeed an eigenvalue-eigenvector pair of A. If it is not, print
        # the message:
        # Not a valid eigenvalue-eigenvector pair of #: ##, ###
        # Where # is A, ## is the eigenvalue, and ### is the eigenvector.
        # And return the boolean False.

    # 9. If all pairs pass the eigenvalue-eigenvector tests for A, return True.


# 10. Apply the check_eigenvector function to the matrix, eigenvectors, and eigenvalues from 3.


