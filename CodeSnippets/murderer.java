public class Person {
	private String name;	
	private boolean alive;
	private boolean murderer;
	private Person myLove;
	
	public Person(String n) {
		alive = true;
		murderer = false;
		name = n;
		System.out.println(this);
	}

	public String getName() { return name; }
	public boolean  isAlive() { return alive; }
	public boolean isMurderer() { return murderer;}
	public void setMurderer(boolean b) { murderer = b;}
	private void suicide() { alive = false; } // Private because a person decides to suicide herself
	
	public void love(Person p) {
		myLove = p;
		if ( this.isMurderer() )
			p.suicide();	// Oops, possible? yes!
	}

	public String toString() {
		return name + " is " + (alive?" alive":" dead");
	}

	public static void main(String args[]) {
		Person aLovedPerson = new Person("Lucy");
		Person aBadPerson = new Person("Al");
		aBadPerson.setMurderer(true);
		System.out.println(aBadPerson.getName() + ".love(" + aLovedPerson.getName() + ");");
		aBadPerson.love(aLovedPerson);
		System.out.println(aLovedPerson);
		System.out.println(aBadPerson);
	}
}