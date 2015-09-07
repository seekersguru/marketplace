/**
 * @description: To create form dynamically.
 * @dependency: jquery1.11.x, bootstrap
 * @verion: 0.1.1
 * @date: 28-Aug-2015
 */
 (function($) {
  'use strict';
 	$.fn.extend({
 		jsonForm: function(options) {
 			options = $.extend({
        formData: {},
        renderData: {},
        formSection: {},
        keyToName: {},
        saveFunction: function (obj) {
          console.log(obj);
        }
      },options);
 			this.each(function() {
 				new $.createJsonForm(this, options);
 			});
 			return this;
 		}
 	});
 	$.createJsonForm = function (me, opt) {
 		var jf = {
 			obj: {
 				$me: $(me)
 			},
 			vr: {
        sectionType: [
          {
            'value': 'key_value',
            'text': 'Key Value'
          },
          {
            'value': 'para',
            'text': 'Paragraph'
          },
          {
            'value': 'packages',
            'text': 'Packages'
          },
          {
            'value': 'map',
            'text': 'Map'
          }
        ],
        selectedSectionType: null
 			},
 			cl: {
 				main: 'json-form',
        gl: 'glyphicon',
				add: 'glyphicon-plus-sign',
				remove: 'glyphicon-minus-sign',
 			},
 			elem: {
 				'input': '<input/>',
 				'button': '<button></button>',
 				'textarea': '<textarea></textarea>',
 				'select': '<select></select>'
 			},
 			func: {
 				init: function () {
          jf.obj.$me.addClass(jf.cl.main);
          jf.func.createTabs(jf.obj.$me);
          jf.func.saveButton(jf.obj.$me);
 				},
        saveButton: function ($container) {
          var $div = $('<div></div>').addClass('footer-bar'),
          $msg = $('<span></span>');
          $msg.appendTo($div);
          $('<button></button>').attr('type', 'button').addClass('btn btn-default').text('Save').click(function() {
            opt.saveFunction(opt.formData, $msg);
          }).appendTo($div);
          $div.appendTo($container);
        },
        createTabs: function ($container) {
          var $ul = $('<ul></ul>').addClass('nav nav-tabs').attr('role','tablist'),
          $li, k, $div = $('<div></div>').addClass('tab-content'), activeClass = ' active',
          fadeClass = ' in';
          for (k in opt.renderData) {
            $li = $('<li></li>').addClass(activeClass);
            $('<a></a>').attr({'href': '#' + k}).attr({
              'role': 'tab',
              'data-toggle': 'tab'
            }).text(opt.formSection[k].name).appendTo($li);
            $li.appendTo($ul);
            jf.func.renderForms(opt.renderData[k], opt.formData[k], $('<div></div>').attr({
              'id': k
            }).addClass('tab-pane fade' + fadeClass + activeClass).appendTo($div), opt.formSection[k].type, k);
            activeClass = '';
            fadeClass = '';
          }
          $ul.appendTo($container);
          $div.appendTo($container);
        },
        renderForms: function (rJson, dJson, $container, type, mainKey) {
          var i = 0, ln, key, keyName, obj, name, required, dataKey, $tab, $li,
          isRender = false, $div = $('<div></div>').addClass('render-form');
          if ('json' === type) {
            for(key in rJson) {
              if ('fix' !== rJson[key]) {
                keyName = rJson[key].split('__');
                if ('{}' === keyName[1]) {
                  obj = dJson[key];
                  name = opt.keyToName[key] || key;
                }
                else if ('[]' === keyName[1]) {
                  obj = dJson[key];
                  name = opt.keyToName[key] || key;
                }
                else if (' ' === keyName[1]) {
                  obj = dJson[key];
                  name = opt.keyToName[key] || key;
                }
                else {
                  obj = dJson[key].value;
                  name = dJson[key].name;
                }
                required = 'req' === keyName[2] ? true : false;
                dataKey = keyName[3];
                jf.func.createForm(obj, name, keyName[0], $div, required, dataKey, mainKey);
                isRender = true;
              }
            }
            if (!isRender) {
              $('<em></em>').text('Form does not exist for this section.').appendTo($div);
            }
          }
          else if ('array' === type) {
            $tab = jf.func.sectionOption($div);
            for (ln = dJson.length; i < ln; i++) {
              jf.func.createSection(dJson[i], $tab, i);
            }
            $li = $tab.find('>ul>li:first').addClass('active');
            $tab.find('>div.tab-content>div' + $li.find('>a').attr('href')).addClass('active in');
          }
          $div.appendTo($container);
        },
        sectionOption: function ($container) {
          var $div = $('<div></div>').addClass('form-div'),
          $tabContainer = $('<div></div>').addClass('section-tabs'),
          $button = $('<button></button>').attr('type', 'button').addClass('btn btn-default').text('Add section').click(function() {
            var $this = $(this), id;
            if (null !== jf.vr.selectedSectionType) {
              id = jf.func.createSection({
                'heading': 'New Section',
                'data_display': [
                  {
                    'type': jf.vr.selectedSectionType
                  }
                ]
              }, $tabContainer, 0);
              $('a[href="#' + id + '"]').click();
              $this.next().text(' ');
            }
            else {
              $this.next().text(' Please choose section type.');
            }
          }),
          $form = $('<form></form>').addClass('form-inline'),
          $fDiv = $('<div></div>').addClass('form-group'),
          $selectDiv = $('<div></div>').addClass('dropdown'),
          $a = $('<a></a>').addClass('dropdown-toggle btn btn-default').attr({
            'data-toggle': 'dropdown',
            'role': 'button'
          }).text('Section Type'), $ul = $('<ul></ul>').addClass('dropdown-menu'),
          i = 0, ln = jf.vr.sectionType.length, $li;
          $a.append(' <span class="caret"></span>');
          $a.appendTo($selectDiv);

          // add options
          for (;i<ln;i++) {
            $li = $('<li></li>');
            $('<a></a>').data('value', jf.vr.sectionType[i].value).attr('href', '#').text(jf.vr.sectionType[i].text).click(function(e) {
              e.preventDefault();
              var $this = $(this), $a = $this.parents('ul.dropdown-menu').prev();
              $a.text($this.text()).append(' <span class="caret"></span>');
              jf.vr.selectedSectionType = $this.data('value');
            }).appendTo($li);
            $li.appendTo($ul);
          }
          $ul.appendTo($selectDiv);
          $selectDiv.appendTo($fDiv);
          $fDiv.appendTo($form);
          $button.appendTo($form.append(' '));
          $('<span></span>').addClass('msg').appendTo($form.append(' '));
          $('<h4></h4>').text('Choose Section Type').appendTo($div);
          $form.appendTo($div);

          // add tab options
          $('<ul></ul>').addClass('nav nav-tabs').appendTo($tabContainer);
          $('<div></div>').addClass('tab-content').appendTo($tabContainer);
          $tabContainer.appendTo($div);
          $div.appendTo($container);
          return $tabContainer;
        },
        createSection: function (obj, $tabContainer, i) {
          var $li = $('<li></li>').addClass('section-link'),
          id = (new Date()).getTime() + i,
          $a = $('<a></a>').attr({'href': '#' + id}).attr({
            'role': 'tab',
            'data-toggle': 'tab'
          }).text(obj.heading).appendTo($li),
          $panel = $('<div></div>').attr('id', id).addClass('tab-pane fade section-panel'),
          $del = $('<a></a>').addClass('del-section').attr('href','#').click(function(e) {
            e.preventDefault();
            jf.func.removeSection($(this));
          }), $div, $form, line1, line2, j = 0, ln = obj.data_display.length;
          $('<span></span>').addClass('glyphicon glyphicon-remove').appendTo($del);
          $del.appendTo($panel);

          // create elements
          $form = $('<form></form>');

          // name of package
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Heading').appendTo($div);
          $('<input/>').attr('type','text').val(obj.heading).addClass('form-control').appendTo($div);
          $div.appendTo($form);
          $form.appendTo($panel);

          for (;j<ln;j++) {
            jf.func.createSectionByType(obj.data_display[j], $panel);
          }

          $li.appendTo($tabContainer.find('>ul'));
          $panel.appendTo($tabContainer.find('>div'));
          return id;
        },
        createSectionByType: function (obj, $container) {
          var i = 0, ln, $form = $('<form></form>'), $div, k;

          if ('key_value' === obj.type) {
            $form.addClass('form-inline key-value-form');
            ln = obj.key_values ? obj.key_values.length : 0;
            $('<label></label>').text('Enter Key/Values').appendTo($('<p></p>').appendTo($form));
            if (0 === ln) {
              for (;i<3;i++) {
                $div = $('<div></div>').addClass('form-group');
                $('<input/>').attr({'type': 'text', 'placeholder': 'Key'}).addClass('form-control').appendTo($div);
                $('<input/>').attr({'type': 'text', 'placeholder': 'Value'}).addClass('form-control').appendTo($div.append(' '));
                $div.appendTo($form);
              }
            }
            else {
              for (;i<ln;i++) {
                for (k in obj.key_values[i]) {
                  $div = $('<div></div>').addClass('form-group');
                  $('<input/>').attr({'type': 'text', 'placeholder': 'Key'}).val(k).addClass('form-control').appendTo($div);
                  $('<input/>').attr({'type': 'text', 'placeholder': 'Value'}).val(obj.key_values[i][k]).addClass('form-control').appendTo($div.append(' '));
                  $div.appendTo($form);
                }
              }
            }
            // read more
            $div = $('<div></div>').addClass('form-group text-right');
            $('<button></button>').attr('type', 'button').addClass('btn btn-success').text('Read More').click(function() {

            }).appendTo($div);
            $div.appendTo($form);
          }
          else if ('para' === obj.type) {
            $div = $('<div></div>').addClass('form-group');
            $('<label></label>').text('Paragraph').appendTo($div);
            $('<textarea></textarea>').attr('rows', 3).val(obj.para).addClass('form-control').appendTo($div);
            $div.appendTo($form);
          }
          else if ('map' === obj.type) {
            $div = $('<div></div>').addClass('form-group');
            $('<label></label>').text('Latitude').appendTo($div);
            $('<input/>').attr('type', 'text').val(obj.lat).addClass('form-control').appendTo($div);
            $div.appendTo($form);

            $div = $('<div></div>').addClass('form-group');
            $('<label></label>').text('Longitude').appendTo($div);
            $('<input/>').attr('type', 'text').val(obj.long).addClass('form-control').appendTo($div);
            $div.appendTo($form);
          }
          else if ('packages' === obj.type) {

          }
          $form.appendTo($container);
        },
        removeSection: function ($me) {
          var $div = $me.parents('div.section-panel'),
          $li = $('a[href="#' + $div.attr('id') + '"]').parent(),
          $nextLi =  $li.siblings('.section-link'), $oLi;
          $oLi = $nextLi.first();
          $oLi.addClass('active');
          $($oLi.find('a').attr('href')).addClass('active in');
          $li.remove();
          $div.remove();
        },
        createForm: function (obj, name, formType, $container, required, dataKey, mainKey) {
          var $div = $('<div></div>').addClass('form-div'),
          $form = $('<form></form>').addClass('');
          $('<h4></h4>').text(name).appendTo($form);
          jf.func.createElem(obj, formType, $form, required, dataKey, mainKey);
          $form.appendTo($div);
          $div.appendTo($container);
        },
        createElem: function (obj, formType, $form, required, dataKey, mainKey) {
          var $div, i = 0, ln, key, $label, $input;
          if ('add_more_package' === formType) {
            $div = $('<div></div>').addClass('package-form');
            jf.func.addMorePackage(obj, $div, required, dataKey, mainKey);
            $div.appendTo($form);
          }
          else if ('add_more_text' === formType) {
            $div = $('<div></div>').addClass('row-form');
            jf.func.addMoreTextElem(obj, $div);
            $div.appendTo($form);
          }
          else if ('checkbox' === formType) {
            $div = $('<div></div>').addClass('checkbox');
            for (ln = obj.length;i<ln;i++) {
              $label = $('<label></label>');
              $('<input/>').attr('type', 'checkbox').prop('checked', true).appendTo($label);
              $label.append(' ' + obj[i][1] + ' ');
              $label.appendTo($div);
            }
            $div.appendTo($form);
          }
          else if ('key_value' === formType) {
            for (key in obj) {
              $div = $('<div></div>').addClass('form-group');
              $('<label></label>').addClass('col-sm-2 control-label').text(opt.keyToName[key] || key).appendTo($div);
              $('<input/>').val(obj[key]).attr('type', 'text').addClass('form-control').appendTo($('<div></div>').addClass('col-sm-10').appendTo($div));
              $div.appendTo($form.addClass('form-horizontal'));
            }
          }
          else if ('textarea' === formType) {
            $div = $('<div></div>').addClass('form-group');
            $('<textarea></textarea>').val(obj).attr('rows',3).addClass('form-control').appendTo($div);
            $div.appendTo($form);
          }
          else if (-1 !== $.inArray(formType, ['text', 'email', 'number', 'url'])) {
            $div = $('<div></div>').addClass('form-group');
            $('<input/>').val(obj).attr('type',formType).addClass('form-control').appendTo($div);
            $div.appendTo($form);
          }
        },
        addMoreTextElem: function (obj, $container) {
          var i = 0, ln = obj.length, $div;
          for (;i<ln;i++) {
            jf.func.createTextElem(obj[i], $container);
          }
          // create atleast one row
          if (0 ===ln) {
            jf.func.createTextElem('', $container, i);
          }
        },
        createTextElem: function (val, $container) {
          var $div = $('<div></div>').addClass('form-group'),
          $innerDiv = $('<div></div>').addClass('add-more'),
          $addRemoveBtn = $('<a></a>').addClass('add-remove-btn').attr('href', '#').click(function (e) {
            e.preventDefault();
						jf.func.addRemoveTextElem(this);
					});
          $('<span></span>').addClass(jf.cl.gl).addClass(jf.cl.add).appendTo($addRemoveBtn);
          $container.find('.' + jf.cl.add).removeClass(jf.cl.add).addClass(jf.cl.remove);
          $('<input/>').addClass('form-control').val(val).attr('type', 'text').appendTo($innerDiv);
          $innerDiv.appendTo($div);
          $addRemoveBtn.appendTo($div);
          $div.appendTo($container);
        },
        removeTextElem: function ($me) {
          $me.parents('div.form-group').remove();
        },
        addRemoveTextElem: function (me) {
          var $me = $(me), $span = $me.children('span');
					if ($span.hasClass(jf.cl.remove)) {
						jf.func.removeTextElem($me);
					}
					else if ($span.hasClass(jf.cl.add)) {
						$span.removeClass(jf.cl.add).addClass(jf.cl.remove);
						jf.func.createTextElem('', $me.parents('div.row-form'));
					}
        },
        addMorePackage: function (obj, $container, required, dataKey, mainKey) {
          var $div = $('<div></div>').addClass('tab-content'),
              $ul = $('<ul></ul>').addClass('nav nav-tabs').attr('role','tablist'),
              $li = $('<li></li>').addClass('pointer'), $oLi, i = 0, ln = obj.length;
          $('<a></a>').attr({'href': '#add'}).attr({
            'role': 'tab',
            'data-toggle': 'tab'
          }).click(function (e) {
            e.preventDefault();
            e.stopPropagation();
            jf.func.addPackage('New Package', {}, $(this).parent()).click();
          }).text('Add Package').appendTo($li);
          $li.appendTo($ul);
          $('<em></em>').text('Click on "Add Package" to add new packages.').appendTo($('<div></div>').attr('id','add').addClass('tab-pane fade package-panel').appendTo($div));
          $ul.appendTo($container);
          $div.appendTo($container);
          for (;i<ln;i++) {
            jf.func.addPackage(obj[i][1], opt.formData[mainKey][dataKey].package_list[obj[i][0]], $li);
          }
          $oLi = $ul.find('li:first');
          $oLi.addClass('active');
          $div.find('>div' + $oLi.find('>a').attr('href')).addClass('active in');
        },
        addPackage: function (packageName, obj, $elem) {
          var $li = $('<li></li>').addClass('package-link'),
          id = (new Date()).getTime(),
          $a = $('<a></a>').attr({'href': '#' + id}).attr({
            'role': 'tab',
            'data-toggle': 'tab'
          }).text(packageName).appendTo($li),
          $panel = $('<div></div>').attr('id', id).addClass('tab-pane fade package-panel'),
          $del = $('<a></a>').addClass('del-package').attr('href','#').click(function(e) {
            e.preventDefault();
            jf.func.removePackage($(this));
          }), $div, $form, line1, line2;
          $('<span></span>').addClass('glyphicon glyphicon-remove').appendTo($del);
          $del.appendTo($panel);

          // create elements
          $form = $('<form></form>');

          // name of package
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Name').appendTo($div);
          $('<input/>').attr('type','text').val(packageName).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          // price of package
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Price').appendTo($div);
          $('<input/>').attr('type','number').val(obj.price).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          // Select Value of package
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Select Value').appendTo($div);
          $('<input/>').attr('type','text').val(obj.select_val).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          // description of package
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Description').appendTo($div);
          $('<textarea></textarea>').val(obj.description).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          // description Url of package
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Desscription Url').appendTo($div);
          $('<input/>').attr('type','url').val(obj.desscription_url).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          // pricing line1 of package
          line1 = obj.pricing && obj.pricing.line1 || '';
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Pricing Line 1').appendTo($div);
          $('<input/>').attr('type','text').val(line1).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          // pricing line2 of package
          line2 = obj.pricing && obj.pricing.line1 || '';
          $div = $('<div></div>').addClass('form-group');
          $('<label></label>').text('Pricing Line 2').appendTo($div);
          $('<input/>').attr('type','text').val(line2).addClass('form-control').appendTo($div);
          $div.appendTo($form);

          $form.appendTo($panel);
          $panel.appendTo($elem.parent().next());
          $li.insertBefore($elem);
          return $a;
        },
        removePackage: function ($me) {
          var $div = $me.parents('div.package-panel'),
          $li = $('a[href="#' + $div.attr('id') + '"]').parent(),
          $nextLi =  $li.siblings('.package-link'), $oLi;
          if ($nextLi.length > 0) {
            $oLi = $nextLi.first();
          }
          else {
            $oLi = $li.siblings('.pointer');
          }
          $oLi.addClass('active');
          $($oLi.find('a').attr('href')).addClass('active in');
          $li.remove();
          $div.remove();
        }
 			},
 			evnt: {
      }
 		};
 		// call init function
 		jf.func.init();
 	};
 })(jQuery);
