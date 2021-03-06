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
    var orderCollection=packages;
   var packagecontainer=$("#packages");
    return {
      getorders: function() {
        packagecontainer.val(JSON.stringify(orderCollection));
        // $("#user_form").submit();
        return orderCollection;
      },
      removeOrder:function(index){
      	$log.info(index);
        packagecontainer.val(JSON.stringify(orderCollection));
        $("#user_form").submit();
      	 orderCollection.splice(index,1);
      },
      addOrder:function(order){
      	$log.info(order);
      	 orderCollection.push(order);
         packagecontainer.val(JSON.stringify(orderCollection));
         $("#user_form").submit();
      },
     editOrder:function(order){
      	$log.info(order);
        packagecontainer.val(JSON.stringify(orderCollection));
        $("#user_form").submit();
      }
    };

  }); 

angular.module('marriageSettingsApp')
  .controller('MainCtrl', function ($scope,$modal,Orders,$rootScope,$http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $("#packages").prependTo('#user_form');
    //list of order which we have save by users
    $scope.orderCollection=Orders.getorders();
    
    $rootScope.userOrder={
      formdata:{
        address:{},
        banquest:{},
        catereres:{},
        decorators:{},
        photographers:{},
        others:{}
      },
      packagedata:{}
    };

$scope.saveform=function(form){

    if(form.$valid)
    {
      alert(JSON.stringify($rootScope.userOrder));
      $http.post('/', $rootScope.userOrder)
          .success(function(data, status, headers, config){

            $scope.status=data.status;

          })
          .error(function(data, status, headers, config){

          });
      }else{
        alert("form not valid bhaya");
      }
};
    $scope.applychange=function(){

    $rootScope.userOrder.formdata.address.name=$('#addresspicker_map').val();
    $rootScope.userOrder.formdata.address.district=$('#city').val();
    $rootScope.userOrder.formdata.address.state=$('#state').val();
    $rootScope.userOrder.formdata.address.country=$('#country').val();
    $rootScope.userOrder.formdata.address.postalcode=$('#pincode').val();
    $rootScope.userOrder.formdata.address.lat=$('#lat').val();
    $rootScope.userOrder.formdata.address.lng=$('#lng').val();
   
    };

    $rootScope.userOrder.packagedata=$scope.orderCollection;


$scope.$watch(
function( $scope ) {

  $rootScope.userOrder.packagedata=$scope.orderCollection;
});
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
			'Jain only'
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
.controller('OrderCtrl', function ($scope, $modalInstance, items ,key,Orders,$rootScope) {

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
    $rootScope.userOrder.packagedata=$scope.orderCollection;
    $modalInstance.close($scope.item);
  };

  $scope.cancel = function () {
     $modalInstance.dismiss('cancel');
  };

  $scope.add = function () {
  	delete $scope.order['menu'];
     Orders.addOrder($scope.order);
    	$scope.orderCollection=Orders.getorders();
      $rootScope.userOrder.packagedata=$scope.orderCollection;
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
      $rootScope.userOrder.packagedata=$scope.orderCollection;
     $modalInstance.close();
  };

  $scope.cancel = function () {
     $modalInstance.dismiss('cancel');
  };


  $scope.getNumber = function(num) {
    return new Array(num);   
	};

});


// override the default input to update on blur
angular.module('app', []).directive('ngModelOnblur', function() {
    return {
        restrict: 'A',
        require: 'ngModel',
        priority: 1, // needed for angular 1.2.x
        link: function(scope, elm, attr, ngModelCtrl) {
            if (attr.type === 'radio' || attr.type === 'checkbox') return;

            elm.unbind('input').unbind('keydown').unbind('change');
            // elm.unbind('input').unbind('keydown').unbind('change');
            elm.bind('blur', function() {
                scope.$apply(function() {
                    ngModelCtrl.$setViewValue(elm.val());
                });         
            });
        }
    };
});