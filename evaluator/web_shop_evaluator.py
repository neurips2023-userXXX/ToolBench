import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "webshop"))

import gym
from rich import print
from rich.markup import escape

from web_agent_site.envs import WebAgentTextEnv

from evaluator import BaseEvaluator


class WebShopEvaluator(BaseEvaluator):
    def __init__(self, generator, max_steps=25):
        super().__init__(generator)
        self.env = gym.make(
            "WebAgentTextEnv-v0", observation_mode="text", num_products=None
        )
        self.max_steps = max_steps

    def __del__(self):
        self.env.close()

    def __call__(self, session_id):
        self.env.reset(session=session_id)
        rewards = [0]
        actions = []
        observation = self.env.observation
        init_observation = observation
        for _ in range(self.max_steps):
            _, action, crash_error = self.get_action(observation)
            if crash_error:
                results = {
                    "crashed": True,
                    "success": False,
                    "query": init_observation,
                    "actions": actions,
                    "reward": rewards[-1],
                    "crashed_error_msg": f"Language model generation error: {str(crash_error)}",
                }
                self.full_results.append(results)
                return results
            actions.append(action)
            observation, reward, done, _ = self.env.step(action)
            print(f'Taking action "{escape(action)}" -> Reward = {reward}')
            rewards.append(reward)
            if done:
                break
        results = {
            "crashed": False,
            "success": done,
            "query": init_observation,
            "actions": actions,
            "reward": rewards[-1],
        }
        self.full_results.append(results)
        return results

    def aggregate_results(self):
        total_crashed = sum([s["crashed"] for s in self.full_results])
        total_success = sum([s["success"] for s in self.full_results])
        total_rewards = sum([s["reward"] for s in self.full_results])
        n_samples = len(self.full_results)
        results = {
            "crash_rate": total_crashed / n_samples,
            "success_rate": total_success / n_samples,
            "reward": total_rewards / n_samples,
        }
        return results
