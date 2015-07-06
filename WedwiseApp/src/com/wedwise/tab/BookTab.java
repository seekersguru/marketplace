package com.wedwise.tab;

import java.util.ArrayList;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.ListView;

import com.wedwise.adapter.MessagesListAdapter;
import com.wedwiseapp.R;
import com.wedwiseapp.util.CustomFonts;

/**
 */
public class BookTab extends Fragment {

	ListView lvBook;
	ArrayList<String> listMessages;
	MessagesListAdapter adapterMessageList;
	Button btnCreateBook;


	@Override
	public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
		View v = inflater.inflate(R.layout.booktab,container,false);
		idInitialization(v);
		return v;
	}

	private void idInitialization(View view)
	{
		lvBook=(ListView) view.findViewById(R.id.lvBook);
		btnCreateBook=(Button) view.findViewById(R.id.btnCreate);
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
		//		CustomFonts.setFontOfButton(getActivity(),btnCreateBook,"fonts/GothamRnd-Light.otf");
		adapterMessageList=new MessagesListAdapter(getActivity(), listMessages);
		lvBook.setAdapter(adapterMessageList);
		lvBook.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				/*Intent myIntent=new Intent(getActivity(),MessageChatActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);*/
			}
		});

		btnCreateBook.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent=new Intent(getActivity(),BidBookCreateActivity.class);
				myIntent.putExtra("type","book");
				startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);		
			}
		});
	}
}