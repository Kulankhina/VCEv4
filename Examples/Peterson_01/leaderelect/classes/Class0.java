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

public abstract class Class0 implements Serializable, BindingController, ElectionItf, Class0AC{

	public boolean isActive = false;
	public int left = 1;
	public int cnum = 1;
	public int max = 1;

	protected Map<String, Object> clItf = new HashMap<String, Object>();
	@Override
	public void bindFc(String myClientItf, Object serverItf) throws NoSuchInterfaceException, IllegalBindingException, IllegalLifeCycleException {
		if(clItf.keySet().contains(myClientItf)) {
			clItf.put(myClientItf, serverItf);
		};
	}

	@Override
	public String[] listFc() {
		return (String[])clItf.keySet().toArray();}

	@Override
	public Object lookupFc(String itf) throws NoSuchInterfaceException {
		return clItf.get(itf);}

	@Override
	public void unbindFc(String itf) throws NoSuchInterfaceException, IllegalBindingException, IllegalLifeCycleException {
		if(clItf.get(itf) != null) {
			clItf.put(itf, null);
		};
	}

	public Class0(){
		super();
		clItf.put("C1", null);
		clItf.put("C2", null);
	}


	public void message(int step, int val) {
		State curState = State.Initial;
		boolean isActive = null;
		int left = null;
		int max = null;
		int cnum = null;

		while(true) {
		switch (curState) {
		case Initial:
			isActive=this.get_isActive();
			curState = State.Choice6;
			break;
		case Choice4:
			if(step == 1) {
				curState = State.Choice5;
				break;
			}
			else if(step == 2) {
				left=this.get_left();
				curState = State.Choice4;
				break;
			}
		case Choice5:
			if(val > max || val < max) {
				((ElectionItf)(clItf.get("C1"))).message(2, val);
				curState = State.State1;
				break;
			}
			else if(val == max) {
				cnum=this.get_cnum();
				curState = State.State10;
				break;
			}
		case State1:
			this.set_left(val);
			curState = State.State11;
			break;
		case Choice4:
			if(left > val && left > max) {
				this.set_max(left);
				curState = State.State3;
				break;
			}
			else if(left <= val || left <= max) {
				this.set_isActive(false);
				curState = State.State9;
				break;
			}
		case State3:
			((ElectionItf)(clItf.get("C1"))).message(1, left);
			curState = State.State11;
			break;
		case State11:
			return ;
			curState = State.Final;
			break;
		case Choice3:
			if(isActive == true) {
				max=this.get_max();
				curState = State.Choice4;
				break;
			}
			else if(isActive == false) {
				((ElectionItf)(clItf.get("C1"))).message(step, val);
				curState = State.State11;
				break;
			}
		case State4:
			this.set_isActive(false);
			curState = State.State11;
			break;
		case State5:
			((LeaderItf)(clItf.get("C2"))).IAmNotTheLeader(cnum);
			curState = State.State11;
			break;
		case Choice6:
			if(step == 1 || step == 2) {
				curState = State.Choice3;
				break;
			}
			else if(step == 0) {
				curState = State.Choice2;
				break;
			}
		case Choice2:
			if(isActive == true) {
				curState = State.State11;
				break;
			}
			else if(isActive == false) {
				this.set_isActive(true);
				curState = State.State6;
				break;
			}
		case State6:
			((ElectionItf)(clItf.get("C1"))).message(0, val);
			curState = State.State7;
			break;
		case State7:
			max=this.get_max();
			curState = State.State8;
			break;
		case State8:
			((ElectionItf)(clItf.get("C1"))).message(1, max);
			curState = State.State11;
			break;
		case State9:
			cnum=this.get_cnum();
			curState = State.State5;
			break;
		case State10:
			((LeaderItf)(clItf.get("C2"))).IAmTheLeader(cnum);
			curState = State.State4;
			break;
		case Final:
			return ;
		default:
			return;
		};
		}

	}
	
	public void set_max(int value) {
		this.max = value;
	}
	
	public int get_left() {
		return this.left;
	}
	
	public void set_left(int value) {
		this.left = value;
	}
	
	public boolean get_isActive() {
		return this.isActive;
	}
	
	public void set_isActive(boolean value) {
		this.isActive = value;
	}
	
	public void set_cnum(int value) {
		this.cnum = value;
	}
	
	public int get_max() {
		return this.max;
	}
	
	public int get_cnum() {
		return this.cnum;
	}
	

}
