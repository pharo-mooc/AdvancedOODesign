{"title" : "Building UI with Spec","slidesid" : "Summer","subtitle" : "An introduction"}# Outline- Spec - Some realization- Concepts- An example of key points# Spec- Application builder- Independent from the back-end \(morphic, GTK, Toplo\)- Build to reuse components \(not shown in this lecture\)# Angular Stone- To build desktop applications fast- Work with different back-ends- All Pharo are ported to Spec20- Can mix low level cairo and high level widgets# A little notepad![ ](figures/spec-tool-iceberg.png width=95)# New browser experiment![ ](figures/spec-tool-browser-experiment.png width=95)# A little notepad![ ](figures/spec-notes-app.png width=95)# Mixing GTK and Cairo![ ](figures/spec-mix-athens-gtk.png width=95)# Thales Covid room allocation![ ](figures/spec-Groom.png width=95)# Key concepts# Spec is based on MVP![ ](figures/spec-MVP.pdf width=95)# Key concepts![ ](figures/spec-coreExtended.pdf width=95)# Key concepts![ ](figures/spec-core.pdf width=95)# Focus on Presenter partA presenter describes- its subcomponents- their configuration - their layout - communication with domain model# ExampleIllustrating key API of \`SpPresenter\`# Example: a simple todo![ ](figures/spec-TodoDone.png width=95)# InitializePresenter```TodoListPresenter >> initializePresenters
	todoListPresenter := self newTable
		addColumn: ((SpCheckBoxTableColumn 
			evaluated: [:task | task isDone]) width: 20);
		addColumn: (SpStringTableColumn 
			title: 'Title' evaluated: [:task | task title]);
		yourself.```# defaultLayout```Smalltalk=trueTodoListPresenter >> defaultLayout
	^ (SpBoxLayout newTopToBottom 
		add: todoListPresenter;
		yourself) ```# Update Presenter```TodoListPresenter >> updatePresenter
    todoListPresenter items: TodoTask tasks```# Initialize window```TodoListPresenter >> initializeWindow: aWindowPresenter

	aWindowPresenter 
		title: 'Todo List';
		initialExtent: 500@500```# Connecting presentersWhen a component is composed of multiple ones, you may need to maintain some invariant.For example, imagine that you have a list of items and an item description text. You may want to always show the description of the selected item.```connectPresenters

	itemList whenSelectionChangedDo: [ :each | description text: each text]```# What we did talk about- Application's role- Component reuse - Styles- Different components \(list, tables, menubar, combox\)- Different Layouts- Menus# Free BookThe forthcoming book freely available at: [https://github.com/SquareBracketAssociates/BuildingApplicationWithSpec2](https://github.com/SquareBracketAssociates/BuildingApplicationWithSpec2)