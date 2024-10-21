
# Challenge
## Caching
### Description

### HRI Locobot

World:
- []
# 1. Observe
raw sensor information --> sensor readings = image, audio, depth

# 2. Hardware
image, audio, depth --> bounding boxes, audio, 

observe()
--> async in a loop
--> 
act(local_state, action) -> local_state

do()

step(state, action) -> state
 calls agent in a loop


EEF Pose
Local State
- sensor information
- odometry
- proprioception


Sense -> hardware's local state (rgb, depth, eef pose, instruction (never empty))
- instruction = (observe your surrounds to understand the world)
- parses instruction to get objects to look for
- vlm description, world, instruction, hardware_state, 
- hardware_local_state
- sensor information
- agents = phi3v

Act -> 

Takes in all the context above and does tree of thought.


Every Agent's job is to fill in its state

Action -> Motors


Each agent can have an act, sense, and think function.
- [ ] 
