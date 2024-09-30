{
	todoListPresenter := self newTable
		addColumn: ((SpCheckBoxTableColumn 
			evaluated: [:task | task isDone]) width: 20);
		addColumn: (SpStringTableColumn 
			title: 'Title' evaluated: [:task | task title]);
		yourself.
	^ (SpBoxLayout newTopToBottom 
		add: todoListPresenter;
		yourself) 
    todoListPresenter items: TodoTask tasks

	aWindowPresenter 
		title: 'Todo List';
		initialExtent: 500@500

	itemList whenSelectionChangedDo: [ :each | description text: each text]