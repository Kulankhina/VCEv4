-- Synch vectors for the assembly of <Comp4_Queue,Comp4_Body, Comp4_runPeterson(), Comp4_message(step, val), Comp4_isActive_ac(), Comp4_left_ac(), Comp4_cnum_ac(), Comp4_max_ac()>
-- with the following input specification:

Structure

<Comp4_Queue,Comp4_Body, Comp4_runPeterson(), Comp4_message(step, val), Comp4_isActive_ac(), Comp4_left_ac(), Comp4_cnum_ac(), Comp4_max_ac()>

Vectors
<  Q_runPeterson  _  _  _  _  _  _  _  > => Queue_runPeterson

<  Serve_runPeterson  Serve_runPeterson  _  _  _  _  _  _  > => Serve_runPeterson

<  _  Call_runPeterson  Call_runPeterson  _  _  _  _  _  > => Call_runPeterson

<  _  R_runPeterson  R_runPeterson  _  _  _  _  _  > => R_runPeterson

<  _  _  Q_message  _  _  _  _  _  > => Q_message

<  _  R_message  _  R_message  _  _  _  _  > => R_message

<  _  _  _  Q_IAmTheLeader  _  _  _  _  > => Q_IAmTheLeader

<  _  _  _  Q_message  _  _  _  _  > => Q_message

<  _  _  _  Q_IAmNotTheLeader  _  _  _  _  > => Q_IAmNotTheLeader

<  _  _  _  Call_get_isActive  Call_get_isActive  _  _  _  > => Call_get_isActive

<  _  _  _  R_get_isActive  R_get_isActive  _  _  _  > => R_get_isActive

<  _  _  _  Call_set_isActive  Call_set_isActive  _  _  _  > => Call_set_isActive

<  _  _  _  Call_set_left  _  Call_set_left  _  _  > => Call_set_left

<  _  _  _  Call_get_left  _  Call_get_left  _  _  > => Call_get_left

<  _  _  _  R_get_left  _  R_get_left  _  _  > => R_get_left

<  _  _  _  Call_get_cnum  _  _  Call_get_cnum  _  > => Call_get_cnum

<  _  _  _  R_get_cnum  _  _  R_get_cnum  _  > => R_get_cnum

<  _  _  _  Call_set_max  _  _  _  Call_set_max  > => Call_set_max

<  _  _  _  Call_get_max  _  _  _  Call_get_max  > => Call_get_max

<  _  _  _  R_get_max  _  _  _  R_get_max  > => R_get_max

<  ErrorQueue  _  _  _  _  _  _  _  > => ErrorQueue

