import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from collections import deque

# Neural Network for Deep Q-Learning
class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Reinforcement Learning Agent
class BotVotingAI:
    def __init__(self, state_size, action_size, learning_rate=0.001, gamma=0.99, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.model = DQN(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        self.criterion = nn.MSELoss()
        
        # Explicit weight factors for adjusting learning behavior
        self.W1 = 1.0  # Weight for frequency of seeing someone
        self.W2 = 1.0  # Weight for proximity to the killed body
        self.W3 = 1.0  # Weight for past behavior influence
        self.W4 = 1.0  # Weight for inconsistent task claims
        self.W5 = 1.0  # Weight for vote tendencies
        self.W6 = 1.0  # Weight for time elapsed since last kill
        
        # Tracking weights and accuracy
        self.weight_history = {f"W{i+1}": [] for i in range(6)}
        self.success_rate_history = []
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
    
    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        act_values = self.model(state_tensor)
        return torch.argmax(act_values).item()
    
    def replay(self, batch_size=32):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            state_tensor = torch.FloatTensor(state)
            next_state_tensor = torch.FloatTensor(next_state)
            target = reward
            if not done:
                target += self.gamma * torch.max(self.model(next_state_tensor)).item()
            target_f = self.model(state_tensor)
            target_f[action] = target
            loss = self.criterion(self.model(state_tensor), target_f)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
        
        # Save weight changes
        self.track_weights()

    def adjust_weights(self, correct_votes, total_votes):
        """Dynamically adjust learning weights based on model performance."""
        accuracy = correct_votes / total_votes if total_votes > 0 else 0
        
        # Adjust weights based on voting success
        self.W1 += 0.1 * (accuracy - 0.5)  # Increase W1 if accuracy is high
        self.W2 += 0.05 * (accuracy - 0.5)
        self.W3 += 0.07 * (accuracy - 0.5)
        self.W4 += 0.08 * (accuracy - 0.5)
        self.W5 += 0.06 * (accuracy - 0.5)
        self.W6 += 0.09 * (accuracy - 0.5)
        
        # Ensure weights stay within reasonable limits
        for i in range(1, 7):
            setattr(self, f"W{i}", max(0.1, min(getattr(self, f"W{i}"), 5.0)))
    
    def track_weights(self):
        for i in range(1, 7):
            self.weight_history[f"W{i}"].append(getattr(self, f"W{i}"))
    
    def track_success_rate(self, correct_votes, total_votes):
        success_rate = correct_votes / total_votes if total_votes > 0 else 0
        self.success_rate_history.append(success_rate)
    
    def plot_progress(self):
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        for i in range(1, 7):
            plt.plot(self.weight_history[f"W{i}"], label=f'W{i}')
        plt.xlabel('Training Iterations')
        plt.ylabel('Weight Magnitude')
        plt.legend()
        plt.title('Weight Adjustments Over Time')

        plt.subplot(1, 2, 2)
        plt.plot(self.success_rate_history, label='Success Rate')
        plt.xlabel('Training Iterations')
        plt.ylabel('Success Rate')
        plt.legend()
        plt.title('Voting Accuracy Over Time')

        plt.show()

# Training Integration with Game Logic
bot_ai = BotVotingAI(state_size=6, action_size=6)  # 6 players excluding you (impostor)

def after_voting_train(state, action, reward, next_state, done, correct_votes, total_votes):
    """Train the RL model immediately after a voting round."""
    # Store experience
    bot_ai.remember(state, action, reward, next_state, done)
    
    # Train the model with experience replay
    bot_ai.replay(batch_size=32)
    
    # Adjust voting behavior weights
    bot_ai.adjust_weights(correct_votes, total_votes)
    
    # Track success rate over iterations
    bot_ai.track_success_rate(correct_votes, total_votes)
    
    # Debugging info
    print(f"Updated weights: {[getattr(bot_ai, f'W{i}') for i in range(1, 7)]}")
    print(f"Latest success rate: {bot_ai.success_rate_history[-1]:.2f}")
    bot_ai.plot_progress()

def bot_vote(state):
    return bot_ai.act(state)
