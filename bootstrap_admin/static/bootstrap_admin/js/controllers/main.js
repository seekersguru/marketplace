'use strict';

/**
 * @ngdoc function
 * @name marriageSettingsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the marriageSettingsApp
 */
angular.module('marriageSettingsApp')
  .factory('Orders', function Order($log) {
    
    //list of order which we have save by users
    var orderCollection=[
			{ 
				'name':'rituraj',
				'type':'Veg',
				'shift':['Morning','Evening'],
				'minpeople':100,
				'maxpeople':200,
		    'quoatedprice':100000,
		    'minprice':10000,
		    'menus':[
		    					{
		    						'name':'name',
		    						'quantity':2,
		    						'options':['paneer pakoda','allo pakoda'],
		    						'example':'test',
		    						'status':true
		    					},{
		    						'name':'name',
		    						'quantity':2,
		    						'options':['paneer pakoda','allo pakoda'],
		    						'example':'test',
		    						'status':true
		    					}


		  				]

				},
  	    {
				
				'name':'Swati',
				'type':'Veg',
				'shift':['Evening'],
				'minpeople':50,
				'maxpeople':2000,
		    'quoatedprice':100000,
		    'minprice':10000,
		    'menus':[
		    					{
		    						'name':'name',
		    						'quantity':2,
		    						'options':['paneer pakoda','allo pakoda'],
		    						'example':'test',
		    						'status':true
		    					},
		    					{
		    						'name':'name',
		    						'quantity':2,
		    						'options':['paneer pakoda','allo pakoda'],
		    						'example':'test'
		    					}
		  			]
			}
	];

    return {
      getorders: function() {
        return orderCollection;
      },
      removeOrder:function(index){
      	$log.info(index);
      	 orderCollection.splice(index,1);
      },
      addOrder:function(order){
      	$log.info(order);
      	 orderCollection.push(order);
      },
     editOrder:function(order){
      	$log.info(order);
      }
    };

  }); 

angular.module('marriageSettingsApp')
  .controller('MainCtrl', function ($scope,$modal,Orders) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    //list of order which we have save by users
    $scope.orderCollection=Orders.getorders();
    //type of menus 
    
    $scope.menusType=[
	    'Welcome Drink',
	    'Starter',
	    'Salad',
	    'Breakfast',
	    'Main Course',
	    'Dal',
	    'Rice',
	    'Raitha',
	    'Keser'
    ];

    // type of food
    
    $scope.foodType=[
			'Veg',
			'Non Veg',
			'Jainokey'
			];

		// type of shift		
    
    $scope.shiftType=[
    	'Morning',
    	'Evening',
    	'Night'
    	];
  
	 // on click of delete button open popup for confirmation
	  
	  $scope.removeItem = function (item,key) {

	    var modalInstance = $modal.open({
	      templateUrl: 'deleteOrder.html',
	      controller: 'OrderCtrl',
	      scope:$scope,
	      backdrop: 'static',	      resolve: {
	        items: function(){
	        return 	item;
	        },
	        key:function(){

	        	return key;
	        }
	      }
	  
	  });
  };

	 // on click of delete button open popup for confirmation
	  
	  $scope.addItem = function () {

	    var modalInstance = $modal.open({
	      templateUrl: 'addOrder.html',
	      controller: 'OrderCtrl',
	      scope:$scope,
	      size:'lg',
	      backdrop: 'static',	
        resolve: {
	        items:'',
	        key:''
	      }
	  
	  });
  };

 $scope.editItem = function (index) {

	    var modalInstance = $modal.open({
	      templateUrl: 'addOrder.html',
	      controller: 'EditOrderCtrl',
	      scope:$scope,
	      size:'lg',
	      backdrop: 'static',	
        resolve: {
	        indexkey:function(){
	        	return index;
	        }
	      }
	  
	  });
  };

});


angular.module('marriageSettingsApp')
.controller('OrderCtrl', function ($scope, $modalInstance, items ,key,Orders) {

  $scope.item = items;

  $scope.order={
  	shift:['Morning'],
  	type:$scope.foodType[0],
  	menus:[
  	// {
  	// 		'name':'Welcome Drink',
			// 	'quantity':2,
			// 	'options':['paneer pakoda','allo pakoda'],
			// 	'example':'test'
			// }
  	]



  };

	angular.forEach($scope.menusType,function(val,key){

  	$scope.order.menus.push({'name':val,'quantity':2,'example':'','status':true});
  
  });

  $scope.order['menu']=[];

  angular.forEach($scope.order.menus,function(val,key){
  	$scope.order.menu.push(val.name);
  });
  
  $scope.integerval = /^\d*$/;

// toggle selection for a given shift by name
  $scope.toggleSelection = function toggleSelection(shiftname) {
    var idx = $scope.order.shift.indexOf(shiftname);

    // is currently selected
    if (idx > -1) {
      $scope.order.shift.splice(idx, 1);
    }

    // is newly selected
    else {
      $scope.order.shift.push(shiftname);
    }
  };

// toggle selection for a given shift by name
  $scope.toggleMenuSelection = function toggleSelection(menuname) {
    var idx = $scope.order.menu.indexOf(menuname);

    // is currently selected
    if (idx > -1) {
      $scope.order.menu.splice(idx, 1);
    }

    // is newly selected
    else {
      $scope.order.menu.push(menuname);
    }
  };

$scope.showMenuSelection = function(menuname) {
     var found = $filter('filter')($scope.order.menus, {id: menuname}, true);
     if (found.length) {
         return 1;
     } else {
				return 0;
	     }
 };
  $scope.delete = function () {
  	Orders.removeOrder(key);
  	// $scope.orderCollection[key];
  	$scope.orderCollection=Orders.getorders();
    $modalInstance.close($scope.item);
  };

  $scope.cancel = function () {
     $modalInstance.dismiss('cancel');
  };

  $scope.add = function () {
  	delete $scope.order['menu'];
     Orders.addOrder($scope.order);
    	$scope.orderCollection=Orders.getorders();
     $modalInstance.close($scope.item);
  };

  $scope.getNumber = function(num) {
    return new Array(num);   
	};

});


angular.module('marriageSettingsApp')
.controller('EditOrderCtrl', function ($scope, $modalInstance, indexkey,Orders) {

$scope.edit=true;

  $scope.order=$scope.orderCollection[indexkey];
  
  $scope.order['menu']=[];

  angular.forEach($scope.order.menus,function(val,key){
  	$scope.order.menu.push(val.name);
  });


  
  $scope.integerval = /^\d*$/;

// toggle selection for a given shift by name
  $scope.toggleSelection = function toggleSelection(shiftname) {
    var idx = $scope.order.shift.indexOf(shiftname);

    // is currently selected
    if (idx > -1) {
      $scope.order.shift.splice(idx, 1);
    }

    // is newly selected
    else {
      $scope.order.shift.push(shiftname);
    }
  };

// toggle selection for a given shift by name
  $scope.toggleMenuSelection = function toggleSelection(menuname) {
    var idx = $scope.order.menu.indexOf(menuname);

    // is currently selected
    if (idx > -1) {
      $scope.order.menu.splice(idx, 1);
    }

    // is newly selected
    else {
      $scope.order.menu.push(menuname);
    }
  };

$scope.showMenuSelection = function(menuname) {
     var found = $filter('filter')($scope.order.menus, {id: menuname}, true);
     if (found.length) {
         return 1;
     } else {
				return 0;
	     }
 };


  $scope.edit = function () {
  	delete $scope.order['menu'];
     Orders.editOrder($scope.order);
    	$scope.orderCollection=Orders.getorders();
     $modalInstance.close();
  };

  $scope.cancel = function () {
     $modalInstance.dismiss('cancel');
  };


  $scope.getNumber = function(num) {
    return new Array(num);   
	};

});


