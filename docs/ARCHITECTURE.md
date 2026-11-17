# Planned architecture

## Problem and audience

A timing volunteer needs to explain why one pilot gained a lap when two gate detections arrived close together.

Audience: FPV club timing volunteers and developers practicing event-driven systems.

## Data flow

1. A fixture reader validates a crossing and associates it with a heat.
2. The ledger records the original event once under its event identifier.
3. The scorer orders crossings by event time and a documented tie-breaker.
4. Marshal rulings annotate disputed crossings by identifier.
5. The standings view and export use the same scorer over the same ledger.

## Important design decisions

### 1. Clock basis

**Choice:** Score integer event timestamps.

**Why:** Replay works without wall time.

**Tradeoff:** Clock skew needs an explicit review rule.

### 2. Corrections

**Choice:** Append rulings to the ledger.

**Why:** Officials can trace decisions.

**Tradeoff:** Every derived report must replay rulings.

### 3. Development inputs

**Choice:** Begin with file fixtures.

**Why:** Anyone can repeat the exercise.

**Tradeoff:** Sensor integration remains a later project.

These are proposed ADRs. Revisit a decision with a concrete measurement or failed requirement; preserve the reason for the change in Git history.
