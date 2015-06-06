package com.calendarapp;

import java.util.ArrayList;

import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.support.v4.app.ActionBarDrawerToggle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v4.widget.DrawerLayout;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.SearchView;
import android.widget.SearchView.OnQueryTextListener;
import android.widget.TextView;

import com.calendar.activity.SubListCategoryActivity;
import com.calendar.adapter.HomeMenuAdapter;
import com.calendar.adapter.Navigationadapter;
import com.calendar.model.ObjectDrawerItem;

public class HomeActivity extends FragmentActivity {

	ListView left_drawer;
	DrawerLayout mDrawerLayout;
	Navigationadapter adapterNavigationDrawer;
	public Context mContext;
	ActionBarDrawerToggle mDrawerToggle;
	ImageButton imgRightMenu,imgLeftMenu;
	SearchView searchView;
	public FragmentManager fragmentManager=null;
	public FragmentTransaction fragmentTransaction=null;
	ListView lvImages;
	HomeMenuAdapter adapterHomeMenu;
	ArrayList<ObjectDrawerItem> listItems;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		//		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.homescreen);
		getActionBar().setTitle("Home");
		mContext=HomeActivity.this;
//		setFragment(new HomeFragment()); 
		lvImages=(ListView) findViewById(R.id.lvImages);
		left_drawer=(ListView) findViewById(R.id.drawer_list);
		mDrawerLayout=(DrawerLayout) findViewById(R.id.drawer_layout);
		searchView=(SearchView) findViewById(R.id.searchView);
		searchView.setQueryHint("Search");
		searchView.setFocusable(false);
		searchView.setFocusableInTouchMode(false);
		int id = searchView.getContext()
				.getResources()
				.getIdentifier("android:id/search_src_text", null, null);
		TextView textView = (TextView) searchView.findViewById(id);
		textView.setTextColor(Color.BLACK);
		textView.setGravity(Gravity.CENTER_VERTICAL);
		int _searchPlateId = searchView.getContext().getResources().getIdentifier("android:id/search_src_text", null, null);
		EditText searchPlate = (EditText) searchView.findViewById(_searchPlateId);
		searchPlate.setGravity(Gravity.CENTER_VERTICAL);

		int searchPlateId = searchView.getContext().getResources().getIdentifier("android:id/search_plate", null, null);
		searchView.findViewById(searchPlateId).setBackgroundResource(R.drawable.nav_white);

		//Navigation Drawer IMplementation
		listItems=new ArrayList<ObjectDrawerItem>();
		/*ObjectDrawerItem item1=new ObjectDrawerItem(R.drawable.weeding_venu_icon, "Wedding Venues");
		listItems.add(item1);
		ObjectDrawerItem item2=new ObjectDrawerItem(R.drawable.bridal_fashion_icon, "Bridal Fashion");
		listItems.add(item2);
		ObjectDrawerItem item3=new ObjectDrawerItem(R.drawable.photogrphers_icon, "Photographers");
		listItems.add(item3);
		ObjectDrawerItem item4=new ObjectDrawerItem(R.drawable.makeup_icon, "Makeup");
		listItems.add(item4);
		ObjectDrawerItem item5=new ObjectDrawerItem(R.drawable.caters_icon, "Caterers");
		listItems.add(item5);
		ObjectDrawerItem item6=new ObjectDrawerItem(R.drawable.flowers_icon, "Flowers");
		listItems.add(item6);
		ObjectDrawerItem item7=new ObjectDrawerItem(R.drawable.discjokey, "Disc jockeys");
		listItems.add(item7);
		ObjectDrawerItem item8=new ObjectDrawerItem(R.drawable.invitation_icon, "invitations");
		listItems.add(item8);*/
		ObjectDrawerItem item1=new ObjectDrawerItem(R.drawable.wedding_venue, "Wedding Venues");
		listItems.add(item1);
		ObjectDrawerItem item2=new ObjectDrawerItem(R.drawable.bridal_fashion, "Bridal Fashion");
		listItems.add(item2);
		ObjectDrawerItem item3=new ObjectDrawerItem(R.drawable.photogrphers, "Photographers");
		listItems.add(item3);
		ObjectDrawerItem item4=new ObjectDrawerItem(R.drawable.makeup, "Makeup");
		listItems.add(item4);
		ObjectDrawerItem item5=new ObjectDrawerItem(R.drawable.caters, "Caterers");
		listItems.add(item5);
		ObjectDrawerItem item6=new ObjectDrawerItem(R.drawable.floweres, "Flowers");
		listItems.add(item6);
		ObjectDrawerItem item7=new ObjectDrawerItem(R.drawable.dsicjokey, "Disc jockeys");
		listItems.add(item7);
		ObjectDrawerItem item8=new ObjectDrawerItem(R.drawable.invitation, "invitations");
		listItems.add(item8);
		adapterHomeMenu=new HomeMenuAdapter(mContext, listItems);
		lvImages.setAdapter(adapterHomeMenu);
		lvImages.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> arg0, View viewChild, int position,
					long arg3) {
				((HomeActivity)mContext).startActivity(new Intent(HomeActivity.this,SubListCategoryActivity.class));
			}
		});
		//		adapterNavigationDrawer=new Navigationadapter(mContext, listItems);
		//		left_drawer.setAdapter(adapterNavigationDrawer);

		/*//***setOnQueryTextFocusChangeListener***
		searchView.setOnQueryTextFocusChangeListener(new View.OnFocusChangeListener() {

			@Override
			public void onFocusChange(View v, boolean hasFocus) {
				// TODO Auto-generated method stub

				Toast.makeText(getBaseContext(), String.valueOf(hasFocus),
						Toast.LENGTH_SHORT).show();
			}
		});*/

		//*** setOnQueryTextListener ***
		searchView.setOnQueryTextListener(new OnQueryTextListener() {

			@Override
			public boolean onQueryTextSubmit(String query) {

				/*Toast.makeText(getBaseContext(), query, 
						Toast.LENGTH_SHORT).show();*/

				return false;
			}

			@Override
			public boolean onQueryTextChange(String newText) {
				// TODO Auto-generated method stub

				/*Toast.makeText(getBaseContext(), newText,
						Toast.LENGTH_SHORT).show();*/
				return false;
			}
		});


		mDrawerToggle = new ActionBarDrawerToggle(
				this,
				mDrawerLayout,
				R.drawable.nav_white, 
				R.string.open, 
				R.string.close
				) {

			/** Called when a drawer has settled in a completely closed state. */
			public void onDrawerClosed(View view) {
				super.onDrawerClosed(view);
				getActionBar().setTitle("");
			}

			/** Called when a drawer has settled in a completely open state. */
			public void onDrawerOpened(View drawerView) {
				super.onDrawerOpened(drawerView);
				getActionBar().setTitle("");
				getActionBar().setDisplayUseLogoEnabled(false);
				getActionBar().setDisplayShowTitleEnabled(false);
				getActionBar().setDisplayShowCustomEnabled(true);
				getActionBar().setBackgroundDrawable(new ColorDrawable(Color.parseColor("#ffffff")));
				getActionBar().setIcon(
						new ColorDrawable(getResources().getColor(android.R.color.transparent)));
				//				getActionBar().setIcon(R.drawable.nav);
			}
		};
		LayoutInflater inflator=(LayoutInflater)this.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
		View v=inflator.inflate(R.layout.header, null);
		imgLeftMenu=(ImageButton) v.findViewById(R.id.imgLeftMenu);
		imgRightMenu=(ImageButton) v.findViewById(R.id.imgRightMenu);
		//		imgLeftMenu.setVisibility(View.INVISIBLE);
		//		mDrawerLayout.setDrawerListener(mDrawerToggle);
		//		mDrawerLayout.openDrawer(Gravity.RIGHT);
		getActionBar().setDisplayHomeAsUpEnabled(true);
		getActionBar().setHomeButtonEnabled(true);
		getActionBar().setDisplayUseLogoEnabled(false);
		getActionBar().setDisplayShowTitleEnabled(false);
		getActionBar().setDisplayShowCustomEnabled(true);
		getActionBar().setBackgroundDrawable(new ColorDrawable(Color.parseColor("#ffffff")));
		getActionBar().setIcon(
				new ColorDrawable(getResources().getColor(android.R.color.transparent)));
		getActionBar().setCustomView(v);
		mDrawerLayout.setClickable(false);
		mDrawerLayout.setOnTouchListener(new OnTouchListener() {

			@Override
			public boolean onTouch(View v, MotionEvent event) {
				mDrawerLayout.closeDrawer(left_drawer);
				return false;
			}
		});
		left_drawer.setClickable(false);
		mDrawerLayout.closeDrawer(left_drawer);
		/*	imgRightMenu.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				if (mDrawerLayout.isDrawerOpen(left_drawer)){
					mDrawerLayout.closeDrawer(left_drawer);
				}
				else{
					mDrawerLayout.openDrawer(left_drawer);	
				}
			}
		});*/
	}

	public void setFragment(Fragment fragment)
	{
		fragmentManager = getSupportFragmentManager();
		fragmentTransaction =fragmentManager.beginTransaction();
		fragmentTransaction.replace(android.R.id.content, fragment);
		fragmentTransaction.addToBackStack(fragment.getClass().getName().substring(fragment.getClass().getName().lastIndexOf(".")+1,fragment.getClass().getName().length()));
		fragmentTransaction.commit();
	}


	@Override
	protected void onPostCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onPostCreate(savedInstanceState);
		mDrawerToggle.syncState();
	}
}
