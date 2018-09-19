package test;



import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.junit.Test;


public class TestLog {
	@Test
	public void testLog() {
		Logger logger=LogManager.getLogger(LogManager.ROOT_LOGGER_NAME);
		logger.debug("debug");
		logger.trace("trace");
		logger.error("err");
	}
	
}
