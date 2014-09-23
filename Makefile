all      :
	@make -C ./src/ all
	@make -C ./doc/ all

clean    :
	@make -C ./src/ clean
	@make -C ./doc/ clean

spotless :
	@make -C ./src/ spotless
	@make -C ./doc/ spotless
