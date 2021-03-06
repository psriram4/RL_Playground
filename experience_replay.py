import numpy as np
import random

class ExperienceReplay():
    def __init__(self, max_buffer_size):
        self.buffer_size = 0
        self.max_buffer_size = max_buffer_size
        self.memory_buffer = []

    def save_transition(self, state, action, reward, next_state, done):
        # if replay memory size exceeded, forget least recent transition
        if self.buffer_size >= self.max_buffer_size:
            self.memory_buffer.pop(0)
            self.buffer_size -= 1

        # save transition as tuple
        transition = (state, action, reward, next_state, done)

        self.memory_buffer.append(transition)
        self.buffer_size += 1

    def sample_memory(self, batch_size):
        if batch_size > self.buffer_size:
            return

        memory_refs = np.arange(self.buffer_size)

        # get indices of randomly sampled transitions
        batch_indices = np.random.choice(memory_refs, batch_size)

        # create batch
        batch = [self.memory_buffer[i] for i in batch_indices]

        return batch
