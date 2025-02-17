---
sidebar_label: What is a throttle?
sidebar_position: 1
---

# ❓ What is a Throttle

The purpose of throttling is to prevent any action from being triggered too many times, thus generating too many alerts.

## Throttle strategies
- [One Until Resolved](one-until-resolved)

## Implementing new strategy
To create a new throttle strategy, create a new class that inherits from `base_throttle.py`, and implements `check_throttling`.

[You can also just submit a new feature request](https://github.com/keephq/keep/issues/new?assignees=&labels=&template=feature_request.md&title=feature:%20new%20throttling%20strategy) and we will get to it ASAP!
