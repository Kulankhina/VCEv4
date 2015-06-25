-- Synch vectors for the assembly of <Comp1_Queue,Comp1_Body, Comp1_message(step, val), Comp1_isActive_ac(), Comp1_left_ac(), Comp1_cnum_ac(), Comp1_max_ac()>
-- with the following input specification:

Structure

<Comp1_Queue,Comp1_Body, Comp1_message(step, val), Comp1_isActive_ac(), Comp1_left_ac(), Comp1_cnum_ac(), Comp1_max_ac()>

Vectors
<  _  R_message  R_message  _  _  _  _  > => R_message

<  _  _  Q_IAmTheLeader  _  _  _  _  > => Q_IAmTheLeader

<  _  _  Q_message  _  _  _  _  > => Q_message

<  _  _  Q_IAmNotTheLeader  _  _  _  _  > => Q_IAmNotTheLeader

<  _  _  Call_get_isActive  Call_get_isActive  _  _  _  > => Call_get_isActive

<  _  _  R_get_isActive  R_get_isActive  _  _  _  > => R_get_isActive

<  _  _  Call_set_isActive  Call_set_isActive  _  _  _  > => Call_set_isActive

<  _  _  Call_set_left  _  Call_set_left  _  _  > => Call_set_left

<  _  _  Call_get_left  _  Call_get_left  _  _  > => Call_get_left

<  _  _  R_get_left  _  R_get_left  _  _  > => R_get_left

<  _  _  Call_get_cnum  _  _  Call_get_cnum  _  > => Call_get_cnum

<  _  _  R_get_cnum  _  _  R_get_cnum  _  > => R_get_cnum

<  _  _  Call_set_max  _  _  _  Call_set_max  > => Call_set_max

<  _  _  Call_get_max  _  _  _  Call_get_max  > => Call_get_max

<  _  _  R_get_max  _  _  _  R_get_max  > => R_get_max

<  ErrorQueue  _  _  _  _  _  _  > => ErrorQueue

