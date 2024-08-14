# Task: Introduction to Eigenvalues and Eigenvectors

# 1. Import numpy with its corresponding alias.



# 2. Initialize a square matrix A to be the following:
# | 4 3 |
# | 1 3 |



# 3. Use the np.linalg.eig function to calculate the eigenvalues and eigenvectors of A.
#    - Save the eigenvalues in a variable called eigenvalues.
#    - Save the eigenvectors_as_cols in a variable called eigenvectors.



# 4. Use a list comprehension to convert eigenvectors_as_cols to a list of eigenvectors.
# Save the output to a variable called eigenvectors.



# 5. Print:
# Eigenvalues: ###
# where ### are the eigenvalues from above.



# 6. Print:
# Eigenvectors as columns: ###
# where ### is the eigenvectors_as_cols variable from above.



# 7. Print:
# List of eigenvectors: ###
# where ### is the list of eigenvectors you created.



# 8. Create a function called check_eigensystem that verifies whether a set of vectors and a set of eigenvalues
# represents the eigensystem of A.
#    - Parameters:
#      - A: The matrix for which the eigenvector is being checked.
#      - eigenvalues: The corresponding list of eigenvalues.
#      - eigenvectors: The list of vectors being tested as eigenvectors.



    # 9. Use a loop and the zip function to iterate through each eigenvalue-eigenvector pair.



        # 10. Use numpy's allclose comparison operator to check if the pair
        # is indeed an eigenvalue-eigenvector pair of A. If it is not, print
        # the message:
        # Not a valid eigenvalue-eigenvector pair of #: ##, ###
        # Where # is A, ## is the eigenvalue, and ### is the eigenvector.
        # And return the boolean False.



    # 11. If all pairs pass the eigenvalue-eigenvector tests for A, return True.




# 12. Apply the check_eigensystem function to the matrix, eigenvectors, and eigenvalues from 5 & 7.


