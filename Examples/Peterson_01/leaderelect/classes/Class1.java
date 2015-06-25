package leaderelect.classes;

import leaderelect.types.*;
import leaderelect.interfaces.*;

import java.util.HashMap;
import java.util.Map;

import org.objectweb.fractal.api.NoSuchInterfaceException;
import org.objectweb.fractal.api.control.BindingController;
import org.objectweb.fractal.api.control.IllegalBindingException;
import org.objectweb.fractal.api.control.IllegalLifeCycleException;


import java.io.Serializable;

public class Class1 extends Class0 implements Serializable, ElectionItf, RunElection, Class1AC{


	public Class1(){
		super();
		clItf.put("C1", null);
		clItf.put("C2", null);
	}


	public void runPeterson() {
		State curState = State.Initial1;

		while(true) {
		switch (curState) {
		case Initial1:
			((ElectionItf)(clItf.get("C1"))).message(0, 1);
			curState = State.State1;
			break;
		case State1:
			return ;
			curState = State.State2;
			break;
		case State2:
			return ;
		default:
			return;
		};
		}

	}
	

}
