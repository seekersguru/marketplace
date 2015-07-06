package com.eventmanagementapp.tab;

import java.util.ArrayList;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

import com.eventmanagementapp.R;
import com.eventmanagementapp.adapter.BookListAdapter;
import com.eventmanagementapp.adapter.MessagesListAdapter;

/**
 */
public class BookTab extends Fragment {

	ListView lvBook;
	ArrayList<String> listMessages;
	BookListAdapter adapterMessageList;

	@Override
	public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
		View v = inflater.inflate(R.layout.booktab,container,false);
		idInitialization(v);
		return v;
	}

	private void idInitialization(View view)
	{
		lvBook=(ListView) view.findViewById(R.id.lvBook);
		listMessages=new ArrayList<String>();
		listMessages.add("Andy Lau");
		listMessages.add("James Moore");
		listMessages.add("Jorgen Flood");
		listMessages.add("Claude");
		listMessages.add("Stefanos Fanidis");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		adapterMessageList=new BookListAdapter(getActivity(), listMessages);
		lvBook.setAdapter(adapterMessageList);
		lvBook.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent=new Intent(getActivity(),BidBookCreateActivity.class);
				myIntent.putExtra("type","book");
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});
	}
}