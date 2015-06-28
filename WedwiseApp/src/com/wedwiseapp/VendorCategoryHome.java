package com.wedwiseapp;

import java.util.ArrayList;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.ListView;
import android.widget.PopupMenu.OnMenuItemClickListener;

import com.wedwise.adapter.AlbumAdapter;
import com.wedwise.tab.MessageTabActivity;
import com.wedwiseapp.login.LoginSignUpActivity;
import com.wedwiseapp.login.RegisterActivity;

public class VendorCategoryHome extends Activity implements
OnMenuItemClickListener {

	// Button btnBack;
	// RecyclerView listRecyclerView;
	ListView lvAlbums;
	AlbumAdapter adapterAlbum;
	ArrayList<String> listItems;
	Button btnHome, btnMenu;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.vendorcategoryhome);
		lvAlbums = (ListView) findViewById(R.id.lvAlbums);
		btnHome = (Button) findViewById(R.id.btnMail);
		btnMenu = (Button) findViewById(R.id.btnMenu);

		listItems = new ArrayList<String>();
		listItems.add("BANQUITE");
		listItems.add("PHOTOGRAPHY");
		listItems.add("CATERERS");
		listItems.add("DECORATORS");
		listItems.add("OTHERS");


		btnMenu.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent = new Intent(VendorCategoryHome.this,
						LoginSignUpActivity.class);
				startActivity(myIntent);

				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

		btnHome.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent = new Intent(VendorCategoryHome.this,
						MessageTabActivity.class);
				startActivity(myIntent);
				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

		adapterAlbum = new AlbumAdapter(VendorCategoryHome.this, listItems);
		lvAlbums.setAdapter(adapterAlbum);

		lvAlbums.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent = new Intent(VendorCategoryHome.this,
						FavListActivity.class);
				startActivity(myIntent);
				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});
	}

	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}

	@Override
	public boolean onMenuItemClick(MenuItem item) {
		switch (item.getItemId()) {
		case R.id.login:

			Intent myIntent = new Intent(VendorCategoryHome.this,
					LoginSignUpActivity.class);
			startActivity(myIntent);
			overridePendingTransition(R.anim.right_in, R.anim.left_out);

			break;
		}
		return true;
	}
}
