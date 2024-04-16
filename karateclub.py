#Gabriela Fuller
#“I have not given or received any unauthorized assistance on this assignment.”

import numpy as np

def analyze_karate_club(interaction_matrix):
    # Verify symmetry of the interaction matrix
    if not np.array_equal(interaction_matrix, interaction_matrix.T):
        raise ValueError("Interaction matrix is not symmetric.")
    
    # Number of members
    num_members = interaction_matrix.shape[0]
    print(f"Number of members: {num_members}")
    
    # Number of interactions per member
    interactions_per_member = np.sum(interaction_matrix, axis=0)
    print("Interactions per member:")
    print(interactions_per_member)
    
    # Least and most active members
    least_active_idx = np.argmin(interactions_per_member)
    most_active_idx = np.argmax(interactions_per_member)
    least_active_interactions = interactions_per_member[least_active_idx]
    most_active_interactions = interactions_per_member[most_active_idx]
    print(f"Least active member index: {least_active_idx}, interactions: {least_active_interactions}")
    print(f"Most active member index: {most_active_idx}, interactions: {most_active_interactions}")
    
    # Average and standard deviation of interactions
    average_interactions = np.mean(interactions_per_member)
    std_interactions = np.std(interactions_per_member)
    print(f"Average interactions: {average_interactions:.2f}")
    print(f"Standard deviation of interactions: {std_interactions:.2f}")

# Load data from file
interaction_matrix = np.loadtxt("karate_club_interactions.txt")

# Analyze the interaction matrix
analyze_karate_club(interaction_matrix)