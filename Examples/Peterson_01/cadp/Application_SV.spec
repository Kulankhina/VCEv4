-- Synch vectors for the assembly of <Application_Queue,Application_Body, Comp1, Comp2, Comp3, Comp4, Scenario>
-- with the following input specification:

Structure

<Application_Queue,Application_Body, Comp1, Comp2, Comp3, Comp4, Scenario>

Vectors
<  Serve_runPeterson  Serve_runPeterson  _  _  _  _  _  > => Serve_runPeterson

<  _  Call_runPeterson  _  _  _  Queue_runPeterson  _  > => Call_runPeterson

<  Serve_IAmTheLeader  _  _  _  _  _  _  > => Q_IAmTheLeader

<  Serve_IAmNotTheLeader  _  _  _  _  _  _  > => Q_IAmNotTheLeader

<  Q_IAmTheLeader  _  _  _  Q_IAmTheLeader  _  _  > => Comp3_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  _  Q_IAmNotTheLeader  _  _  > => Comp3_Q_IAmNotTheLeader

<  Q_IAmTheLeader  _  Q_IAmTheLeader  _  _  _  _  > => Comp1_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  Q_IAmNotTheLeader  _  _  _  _  > => Comp1_Q_IAmNotTheLeader

<  Q_IAmTheLeader  _  _  Q_IAmTheLeader  _  _  _  > => Comp2_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  Q_IAmNotTheLeader  _  _  _  > => Comp2_Q_IAmNotTheLeader

<  Q_IAmTheLeader  _  _  _  _  Q_IAmTheLeader  _  > => Comp4_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  _  _  Q_IAmNotTheLeader  _  > => Comp4_Q_IAmNotTheLeader

<  _  _  Queue_message  _  _  Q_message  _  > => Comp4_Comp1_Q_message

<  _  _  _  _  Q_message  Queue_message  _  > => Comp3_Comp4_Q_message

<  _  _  Q_message  Queue_message  _  _  _  > => Comp1_Comp2_Q_message

<  _  _  _  Q_message  Queue_message  _  _  > => Comp2_Comp3_Q_message

<  Q_runPeterson  _  _  _  _  _  Q_runPeterson  > => Scenario_runPeterson

<  _  _  _  _  _  _  Call_Scenario  > => Call_Scenario

<  _  _  _  _  ErrorQueue  _  _  > => Comp3_ErrorQueue

<  _  _  ErrorQueue  _  _  _  _  > => Comp1_ErrorQueue

<  _  _  _  ErrorQueue  _  _  _  > => Comp2_ErrorQueue

<  _  _  _  _  _  ErrorQueue  _  > => Comp4_ErrorQueue

<  ErrorQueue  _  _  _  _  _  _  > => Application_ErrorQueue

