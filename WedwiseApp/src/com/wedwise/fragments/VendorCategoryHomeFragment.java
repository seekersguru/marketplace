package com.wedwise.fragments;

import java.util.ArrayList;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.ListView;
import com.wedwise.adapter.AlbumAdapter;
import com.wedwise.tab.MessageTabActivity;
import com.wedwiseapp.FavListActivity;
import com.wedwiseapp.NavigationDrawerHomeActivity;
import com.wedwiseapp.R;
import com.wedwiseapp.login.LoginSignUpActivity;

public class VendorCategoryHomeFragment extends Fragment{

	ListView lvAlbums;
	AlbumAdapter adapterAlbum;
	ArrayList<String> listItems;
	Button btnHome, btnMenu;
	Context mContext;

	@Override
	public View onCreateView(LayoutInflater inflater, ViewGroup container,
			Bundle savedInstanceState) {
		View rootView = inflater.inflate(R.layout.vendorcategoryhome, container, false);
		mContext = getActivity();
		idInitialization(rootView);
		return rootView;
	}

	private void idInitialization(View rootView)
	{
		lvAlbums = (ListView)rootView.findViewById(R.id.lvAlbums);
		btnHome = (Button)rootView.findViewById(R.id.btnMail);
		btnMenu = (Button)rootView.findViewById(R.id.btnMenu);

		listItems = new ArrayList<String>();
		listItems.add("BANQUITE");
		listItems.add("PHOTOGRAPHY");
		listItems.add("CATERERS");
		listItems.add("DECORATORS");
		listItems.add("OTHERS");
		btnMenu.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent = new Intent(getActivity(),
						LoginSignUpActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

		btnHome.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent = new Intent(getActivity(),
						MessageTabActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

		adapterAlbum = new AlbumAdapter(mContext, listItems);
		lvAlbums.setAdapter(adapterAlbum);

		lvAlbums.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent = new Intent(getActivity(),
						FavListActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

	}
}
